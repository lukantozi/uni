function getAllCalendars() {
  const cals = CalendarApp.getAllCalendars().map(cal => ({
    ID: cal.getId(),
    NAME: cal.getName(),
    TIME_ZONE: cal.getTimeZone()
  }));
  Logger.log(JSON.stringify(cals, null, 2));
}

function createEventsInNewCalendar() {
  const calendarName = 'My sre practice Calendar';
  const calendar =
      CalendarApp.getCalendarsByName(calendarName)?.[0] ||
      CalendarApp.createCalendar(calendarName)
        .setColor(CalendarApp.Color.RED_ORANGE);

  const events = [
    {
      title: 'Event 1',
      startTime: new Date(2024, 8, 1, 11, 0),
      endTime: new Date(2024, 8, 1, 12, 0),
    },
    {
      title: 'Event 2',
      startTime: new Date(2024, 8, 1, 13, 30),
      endTime: new Date(2024, 8, 1, 14, 30),
    },
    {
      title: 'Event 3',
      startTime: new Date(2024, 8, 1, 15, 0),
      endTime: new Date(2024, 8, 1, 17, 15),
    }
  ];

  events.forEach(e => calendar.createEvent(e.title, e.startTime, e.endTime));
}

function getEvents() {
  const calendarName = 'My Apps Script Calendar';
  const calendar = CalendarApp.getCalendarsByName(calendarName)?.[0];

  const date = new Date(2024, 8, 1);
  const events = calendar.getEventsForDay(date);

  Logger.log(
    JSON.stringify(
      events.map(e => ({
        title: e.getTitle(),
        startTime: e.getStartTime(),
        endTime: e.getEndTime(),
      })),
      null,
      2
    )
  );
}

function inviteGuests() {
  const calendarName = 'My Apps Script Calendar';
  const calendar = CalendarApp.getCalendarsByName(calendarName)?.[0];
  const date = new Date(2024, 8, 1);

  const guests = [
    { eventName: 'Event 1', guestEmails: ['luka+test1@gmail.com'] },
    { eventName: 'Event 2', guestEmails: ['luka+test2@gmail.com'] },
    { eventName: 'Event 3', guestEmails: ['luka+test3@gmail.com'] },
  ];

  calendar.getEventsForDay(date).forEach(event => {
    const guestList = guests.find(g => g.eventName === event.getTitle());
    if (guestList === undefined) return;
    guestList.guestEmails.forEach(email => event.addGuest(email));
  });
}

class AgendaExtractor {
  constructor(calendarName = null) {
    this.calendarName = calendarName;
    this.calendar =
      null === calendarName
        ? CalendarApp.getDefaultCalendar()
        : CalendarApp.getCalendarsByName(calendarName)?.[0];

    if (!this.calendar) throw new Error('Could not access calendar');
  }

  getEvents(startTimeOrDay, endTime = null) {
    this.events =
      null !== endTime
        ? this.calendar.getEvents(startTimeOrDay, endTime)
        : this.calendar.getEventsForDay(startTimeOrDay);
    return this;
  }

  extractFieldsAsTwoDimArray() {
    const twoDimAr = this.events.map(event => [
      Utilities.formatDate(event.getStartTime(), 'GMT', 'HH:mm:ss'),
      event.getTitle(),
      event.getGuestList().length,
    ]);
    return [['Start Time', 'Title', 'Number of Guests'], ...twoDimAr];
  }
}

class TemplateMerger {
  constructor(templateName) {
    this.templateName = templateName;
  }

  toHtmlTable(twoDimAr) {
    const thStyle =
      'style="padding: 10px; text-align: left; border-bottom: 1px solid #dddddd; background-color: #f2f2f2;"';
    const tdStyle =
      'style="padding: 10px; text-align: left; border-bottom: 1px solid #dddddd;"';

    const headers = twoDimAr.shift();

    const th =
      '<tr>' +
      headers.map(header => `<th ${thStyle}>${header}</th>`).join('') +
      '</tr>';

    const td = twoDimAr
      .map(
        row =>
          '<tr>' +
          row.map(cell => `<td ${tdStyle}>${cell}</td>`).join('') +
          '</tr>'
      )
      .join('');

    this.table = `<table style="width: 100%; border-collapse: collapse;"><thead>${th}</thead><tbody>${td}</tbody></table>`;
    return this;
  }

  mergeTemplate(mergeField) {
    return HtmlService.createHtmlOutputFromFile(this.templateName)
      .getContent()
      .replace(new RegExp(`{{${mergeField}}}`), this.table);
  }
}

class Emailer {
  constructor(recipients = []) {
    this.recipients = recipients;
  }

  setSubject(subject) {
    this.subject = subject;
    return this;
  }

  setContent(html) {
    this.content = html;
    return this;
  }

  send() {
    GmailApp.sendEmail(this.recipients.join(','), this.subject, '', {
      htmlBody: this.content,
    });
  }
}

function sendAgenda() {
  const date = new Date();
  const day = Utilities.formatDate(new Date(), 'GMT', 'yyyy-MM-dd');
  const calendarName = 'My Apps Script Calendar';

  const agenda = new AgendaExtractor(calendarName)
    .getEvents(date)
    .extractFieldsAsTwoDimArray();

  const html = new TemplateMerger('AgendaTemplate')
    .toHtmlTable(agenda)
    .mergeTemplate('TABLE');

  new Emailer(['luka+agenda@gmail.com'])
    .setSubject(`Agenda for ${day}`)
    .setContent(html)
    .send();
}

function manageEventAccess() {
  const calendarName = 'My Apps Script Calendar';
  const calendar = CalendarApp.getCalendarsByName(calendarName)?.[0];
  const event = calendar.getEventsForDay(new Date(2024, 8, 1))[0];

  event.addGuest('lmamrikishvili01@gmail.com');

  event.removeGuest('lmamrikishvili01@gmail.com');

  event.setAnyoneCanAddSelf(true);
  event.setGuestsCanInviteOthers(true);
  event.setGuestsCanModify(false);
  event.setGuestsCanSeeGuests(true);

  event.setVisibility(CalendarApp.Visibility.PRIVATE);

  Logger.log('Access settings updated for event: ' + event.getTitle());
}
