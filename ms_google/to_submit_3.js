// ms-google_lecture_3
function myFunction() {
  const a1 = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet().getRange('A1').getValue();
  Logger.log(a1);
}


function doGet() {
  const ssid = "1vC7qI1_9uz0nsDaxQlF4r1WlOB3iXeB5GYOcshsYBj0"
  const a1 = SpreadsheetApp.openById(ssid).getSheets()[0].getRange('a1').getValue();
  return HtmlService.createHtmlOutput('<h1>' + a1 + '<h1>')
}
