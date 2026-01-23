function setUpForm() {
  const form = FormApp.getActiveForm();

  form
    .setTitle('Test Form')
    .setDescription('This form is managed by Apps Script')
    .setCollectEmail(true);

  form.getItems().forEach(item => form.deleteItem(item.getIndex()));

  form
    .addTextItem()
    .setRequired(true)
    .setTitle('Name')
    .setHelpText('Your first name');

  Logger.log(`Published URL: ${form.getPublishedUrl()}`);
  return form;
}

function getResponses() {
  const form = FormApp.getActiveForm();

  form.getResponses().forEach(response => {
    const respondent = response.getRespondentEmail();
    Logger.log(`We have a response from ${respondent}`);

    response.getItemResponses().forEach(item => {
      const title = item.getItem().getTitle();
      const responseValue = item.getResponse();
      Logger.log(`* They answered ${responseValue} to ${title}`);
    });
  });
}

function submitProgrammaticResponse() {
  const form = FormApp.getActiveForm();

  const programmaticFormResponse = form.createResponse();

  const item = form.getItems()[0];
  const programmaticItemResponse = item.asTextItem().createResponse('Luka');

  programmaticFormResponse
    .withItemResponse(programmaticItemResponse)
    .submit();
}

function resetAsEesForm(hardReset = false) {
  const form = FormApp.getActiveForm();

  if (hardReset) form.deleteAllResponses();

  form
    .setTitle('Employee Engagement Survey')
    .setDescription('This form is managed by Apps Script')
    .setCollectEmail(false);

  form.getItems().forEach(item => form.deleteItem(item.getIndex()));

  return form;
}

function SatisfactionSection(form = FormApp.getActiveForm()) {
  form
    .addSectionHeaderItem()
    .setTitle('Overall Satisfaction and Work Environment')
    .setHelpText('This section aims to understand your overall satisfaction with the company and gather feedback on your work environment.');

  form
    .addScaleItem()
    .setTitle('On a scale of 1 to 5, how satisfied are you with your overall experience working at our company?')
    .setHelpText('Scale: 1 - Very Dissatisfied to 5 - Very Satisfied')
    .setBounds(1, 5)
    .setRequired(true);

  const env = form
    .addMultipleChoiceItem()
    .setTitle('How would you rate your work environment?')
    .setHelpText('Include physical workspace, tools, and resources')
    .setRequired(true);

  env.setChoices(
    ['Excellent', 'Good', 'Average', 'Poor', 'Very Poor'].map(choice => env.createChoice(choice))
  );

  form
    .addTextItem()
    .setTitle('What improvements, if any, would you suggest for your work environment?')
    .setHelpText('Free text')
    .setRequired(false);
}

function EngagementSection(form = FormApp.getActiveForm()) {
  form
    .addSectionHeaderItem()
    .setTitle('Engagement and Company Culture')
    .setHelpText('This section evaluates your engagement with the company and your perspective on the overall company culture.');

  form
    .addScaleItem()
    .setBounds(1, 5)
    .setTitle('How engaged do you feel with your work and the company?')
    .setHelpText('Scale: 1 - Not Engaged at All to 5 - Highly Engaged')
    .setRequired(true);

  form
    .addMultipleChoiceItem()
    .setTitle('Would you recommend our company as a great place to work?')
    .setChoiceValues(['Yes', 'No'])
    .setRequired(true);

  form
    .addTextItem()
    .setTitle('How engaged do you feel with your work and the company?')
    .setHelpText('Minimum length: 100 characters')
    .setValidation(
      FormApp.createTextValidation()
        .requireTextLengthGreaterThanOrEqualTo(100)
        .build()
    )
    .setRequired(true);
}

function main() {
  const form = resetAsEesForm(true);
  SatisfactionSection(form);
  EngagementSection(form);
}

function addSections(callbacks, form = FormApp.getActiveForm(), options = {}) {
  if (!Array.isArray(callbacks)) throw 'Array of callbacks was not provided';

  callbacks.forEach((cb, i) => {
    cb instanceof Function && cb(form);

    if (options.addPageBreaks && i < callbacks.length - 1) {
      form.addPageBreakItem().setTitle(`Page ${i + 2} of ${callbacks.length}`);
    }
  });
}

function main() {
  const form = resetAsEesForm(true);
  addSections([SatisfactionSection, EngagementSection], form, {
    addPageBreaks: true,
  });
}

function getScores() {
  const form = FormApp.getActiveForm();

  const responses = form.getResponses().map(response => {
    const irs = response.getItemResponses();

    return irs.reduce((acc, ir) => {
      if (ir.getItem().getType() !== FormApp.ItemType.SCALE) return acc;

      const title = ir.getItem().getTitle();
      const answer = ir.getResponse();

      if (/satisfied/.test(title)) acc.satisfaction = answer;
      if (/engaged/.test(title)) acc.engagement = answer;

      return acc;
    }, {});
  });

  const averages = responses.reduce(
    (sum, resp) => {
      sum.satisfaction += +resp.satisfaction;
      sum.engagement += +resp.engagement;
      return sum;
    },
    { satisfaction: 0, engagement: 0 }
  );

  averages.satisfaction /= responses.length;
  averages.engagement /= responses.length;

  console.log(averages);
  return averages;
}

function configureRespondentAccess() {
  const form = FormApp.getActiveForm();

  form.setAcceptingResponses(true);

  form.setAllowResponseEdits(true);

  form.setCollectEmail(true);

  form.setRequireLogin(true);
}
