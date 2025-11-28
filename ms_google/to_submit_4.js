function createNewSpreadsheet() {
    const newSpreadsheet = SpreadsheetApp.create('Created with Google Apps Script');
    const spreadsheetUrl = newSpreadsheet.getUrl();
    Logger.log(spreadsheetUrl);
}

function retrieveSpreadsheetOwner() {
    const sheet = SpreadsheetApp.getActiveSpreadsheet();
    const owner = sheet.getOwner(); 
    Logger.log('This spreadsheet is owned by ' + owner.getEmail());
}

function addViewerEdit() {
    const sheet = SpreadsheetApp.getActiveSpreadsheet();
    sheet
        .addViewer('john.doe@company.com')
        .addEditor('jane.doe@company.com');
}

function getRenameSpreadSheet() {
    const sheet = SpreadsheetApp.getActiveSpreadsheet();
    Logger.log(sheet.getName());
    sheet.rename('New Sheet Name');
    Logger.log(sheet.getName());
}

function getNumberOfSheets() {
    const sheet = SpreadsheetApp.getActiveSpreadsheet();
    const numSheets = sheet.getNumSheets();
    Logger.log(`This spreadsheet contains ${numSheets} sheets`);
}

function setTheLocal() {
    const sheet = SpreadsheetApp.getActiveSpreadsheet();
    const locale = sheet.getSpreadsheetLocale();
    Logger.log(`This document's locale is ${locale}`);
}

function timeZone() {
    const sheet = SpreadsheetApp.getActiveSpreadsheet();
    const timeZone = sheet.getSpreadsheetTimeZone();
    Logger.log(`This document's time zone is ${timeZone}`);
}

function getUrl() {
    const url = SpreadsheetApp.getActiveSpreadsheet().getUrl();
    Logger.log(url);
}

function createNewSheet() {
    const spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
    spreadsheet.insertSheet();
}

function createNewSheet() {
    const ss = SpreadsheetApp.getActiveSpreadsheet();
    const templateSheet = ss.getSheetByName('Sheet1');
    ss.insertSheet(1, { template: templateSheet });
}

function getSheetByName(sheetName) {
    return SpreadsheetApp
        .getActiveSpreadsheet()
        .getSheetByName(sheetName);
}

function getSheetByIndex(sheetIndex) {
    return SpreadsheetApp
        .getActiveSpreadsheet()
        .getSheets()[sheetIndex];
}

function main_1() {
    const sheet1 = getSheetByName('Sheet1');

    const sheet2 = getSheetByIndex(0);
}

function getSheet(indexOrName) {
    const spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
    if ('string' === typeof indexOrName) return spreadsheet.
        getSheetByName(indexOrName);
    if ('number' === typeof indexOrName) return spreadsheet.
        getSheets()[indexOrName];
    return null;
}

function main_2() {
    const sheet1 = getSheet('Sheet1');
    Logger.log(sheet1.getName());

    const sheet2 = getSheet(0);
    Logger.log(sheet2.getName());
}

function getSheet(indexOrName) {
    const spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
    if ('string' === typeof indexOrName) {
        return spreadsheet.getSheetByName(indexOrName);
    } else if ('number' === typeof indexOrName) {
        return spreadsheet.getSheets()[indexOrName];
    } else {
        return null;
    }
}

function getLastRowAndColumn() {
    const sheet1 = SpreadsheetApp
        .getActiveSpreadsheet()
        .getSheetByName('Sheet1');

    const lastRow = sheet1.getLastRow();
    const lastColumn = sheet1.getLastColumn();

    Logger.log(`Sheet "${sheet1.getName()}" contains ${lastRow} rows and ${lastColumn} columns`);
}
