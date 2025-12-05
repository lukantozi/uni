function myFunction () {
    const recipient = 'lukamamrik@proton.me';
    const subject = 'Hello world!';
    const body = 'Sent with GmailApp.';
    GmailApp.sendEmail(recipient, subject, body);
}

function myFunction () {
    const sentMessage = GmailApp
        .createDraft(recipient, subject, body)
        .send()
        .star();
}

function myFunction () {
    GmailApp.createDraft('lukamamrik@proton.me', 'New Draft', 'Created with GmailApp');
}

function listDrafts() {
    const drafts = GmailApp.getDrafts();
    drafts.forEach(draft => Logger.log(draft.getMessage().getSubject()));
}

function updateDrafts() {
    const re = /Created with GmailApp/i;
    const newRecipients = ['lukamamrik@proton.me', 'lukamamri@outlook.com'];
    GmailApp.getDrafts().forEach(draft => {
        const message = draft.getMessage();
        const body = message.getBody();
        if (!re.test(body)) return;
        const to = message.getTo();
        const subject = message.getSubject();
        const newSubject = `${subject} renamed by Apps Script`;
        const newTo = `${to},${newRecipients.join(', ')}`;
        draft.update(newTo, newSubject, body);
        Logger.log(`Successfully renamed "${subject}" to "${newSubject}" and added the following recipients: ${newRecipients.join(', ')}`);
    });
}

function updateDrafts() {
    const re = /Created with GmailApp/i;
    const newRecipients = ['lukamamrik@proton.me', 'lukamamri@outlook.com'];
    const carbonCopy = ['alex@example.com', 'murphy@example.com'];
    GmailApp.getDrafts().forEach(draft => {
        const message = draft.getMessage();
        const body = message.getBody();
        if (!re.test(body)) return;
        const to = message.getTo();
        const subject = message.getSubject();
        const newSubject = `${subject} renamed by Apps Script`;
        const newTo = `${to},${newRecipients.join(', ')}`;
        const htmlBody = '<p><span style="color: red;">Created with</span> <b>GmailApp</b></p>';
        draft.update(newTo, newSubject, body, {htmlBody, cc: carbonCopy.join(', ')});
    });
}

function readEmails() {
    const threads = GmailApp.getInboxThreads();
    let threadsRead = 0;
    const maxThreads = 5;
    for (let i = 0; i < threads.length; i++) {
        if (threadsRead >= maxThreads) break;
        const thread = threads[i];
        const numMessages = thread.getMessageCount();
        if (numMessages < 3 || numMessages > 5) continue;
        const subject = thread.getFirstMessageSubject();
        Logger.log(`Found thread "${subject}" with ${numMessages} messages`);
        const messages = thread.getMessages();
        messages.forEach((message, i) => {
            Logger.log(`Message ${i + 1} ${message.getFrom()} to ${message.getTo()}`);
        });
        threadsRead++;
    }
}

function findEmails() {
    const searchQuery = 'in:inbox from:tldr is:unread';
    const threads = GmailApp.search(searchQuery);
    threads.forEach(thread => {
        const subject = thread.getFirstMessageSubject();
        Logger.log(subject);
        thread.addLabel(getLabel('TLDR'));
    });
}

function getLabel(text) {
    const label = GmailApp.getUserLabelByName(text);
    if (label) return label;
    return GmailApp.createLabel(text);
}

class Records {
    constructor(sheetName) {
        this.spreadsheet = SpreadsheetApp.getActive();
        this.sheetName = sheetName;
        this.worksheet = this.spreadsheet.getSheetByName(this.sheetName);
        if (null === this.worksheet)
            throw `Worksheet ${this.sheetName} does not exist`;
        this.data = this.worksheet.getDataRange().getDisplayValues();
        this.headers = this.data.shift();
        this.records = this.data.map(row =>
            row.reduce(
                (record, value, i) => ({ ...record, [this.headers[i]]: value }),
                {}
            )
        );
    }
}

const EMAIL_SETTINGS = {
    subject: '{{Recipient Name}}, you are invited to the {{Event Name}}',
    toField: 'Email Address',
    resultsField: 'Invitation Sent (Y/N)'
};

Object.freeze(EMAIL_SETTINGS);

function createEmails() {
    const htmlTemplate =
        HtmlService.createHtmlOutputFromFile('EmailTemplate').getContent();
    const rec = new Records('Invitees');
    const results = [];
    rec.records.forEach(record => {
        let htmlBody = htmlTemplate;
        let subject = EMAIL_SETTINGS.subject;
        const to = record[EMAIL_SETTINGS.toField];
        Object.entries(record).forEach(([key, value]) => {
            htmlBody = htmlBody.replace(new RegExp(`{{${key}}}`, 'g'), value);
            subject = subject.replace(new RegExp(`{{${key}}}`, 'g'), value);
        });
        try {
            GmailApp.createDraft(to, subject, '', { htmlBody });
            results.push('Y');
        } catch (err) {
            Logger.log(`ERROR trying to send to ${to}: ${err}`);
            results.push('N');
        }
    });
    Logger.log(results);
    return { rec, results };
}

function updateResultsInSheet({ rec, results }) {
    const colIndex = rec.headers.findIndex(
        header => EMAIL_SETTINGS.resultsField === header
    );
    if (-1 === colIndex)
        throw `Could not find column "${EMAIL_SETTINGS.resultsField}" in sheet ${rec.sheetName}`;
    const range = rec.worksheet
        .getRange(2, colIndex + 1, results.length, 1)
        .setValues(results.map(result => [result]));
}

function merge() {
    const mergeResults = createEmails();
    updateResultsInSheet(mergeResults);
}
