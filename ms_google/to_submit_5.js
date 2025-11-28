function getSheet(indexOrName) {
    const spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
    if ('string' === typeof indexOrName) return spreadsheet.getSheetByName(indexOrName);
    if ('number' === typeof indexOrName) return spreadsheet.getSheets()[indexOrName];
    return null;
}

function addNewRow() {
    const row = [
        'Priya',
        'Aurora',
        43,
        'Scrum Master',
        'IT',
        '2024-01-08'
    ];
    const sheet = getSheet(0);
    sheet.appendRow(row);
}

function removeAnalysts() {
    const sheet = getSheet(0);
    const numRows = sheet.getLastRow();
    const professionColumn = 4;
    for (let i = 1; i <= numRows; i++) {
        const profession = sheet.getRange(i, professionColumn).getValue();
        if (profession.includes('Analyst')) sheet.deleteRow(i);
    }
}

function extractValues() {
    const sheet = getSheet(0);
    const lastRow = sheet.getLastRow();
    const lastColumn = sheet.getLastColumn();
    const range = sheet.getRange(1, 1, lastRow, lastColumn);

    const values = range.getValues();
    Logger.log(JSON.stringify(values, null, 2));
}

function extractValuesSimplified() {
    const sheet = getSheet(0);
    const range = sheet.getDataRange();
    const values = range.getValues();
    Logger.log(JSON.stringify(values, null, 2));
}


function getDifferenceInDays(date1, date2) {
    date1 = (date1 instanceof Date) ? date1 : new Date(date1);
    date2 = (date2 instanceof Date) ? date2 : new Date(date2);

    const timeDiff = Math.abs(date2.getTime() - date1.getTime());
    const diffDays = Math.ceil(timeDiff / (1000 * 3600 * 24));
    return diffDays;
}

function insertEmploymentDays() {
    const daysEmployed = [['Days Employed']];

    const sheet = getSheet(0);
    const lastRow = sheet.getLastRow();
    const lastColumn = sheet.getLastColumn();
    const range = sheet.getRange(1, 1, lastRow, lastColumn);
    const values = range.getValues();

    const now = new Date();

    const employmentDateIndex = 5;

    for (let i = 1; i < values.length; i++) {
        const employmentDate = values[i][employmentDateIndex];

        const daysAtWork = getDifferenceInDays(employmentDate, now);

        daysEmployed.push([daysAtWork]);
    }

    sheet
        .getRange(1, lastColumn + 1, daysEmployed.length, daysEmployed[0].length)
        .setValues(daysEmployed);
}

function twoDimArrayLength() {
    const warehouseData = [
        ["Item ID", "Item Name", "Quantity"],
        ["101", "Screwdrivers", 150],
        ["102", "Hammers", 85],
        ["103", "Wrenches", 200]
    ];

    Logger.log(`Number of rows: ${warehouseData.length}`);
    Logger.log(`Number of columns: ${warehouseData[0].length}`);
}

function loopOver2DArray() {
    const pharmacySalesData = [
        ['Medicine', 'Quantity Sold', 'Revenue'],
        ['Aspirin', 100, 2000],
        ['Paracetamol', 150, 3000],
        ['Ibuprofen', 80, 1600],
    ];

    const bestSellers = [['Medicine', 'Quantity Sold']];

    for (let i = 0; i < pharmacySalesData.length; i++) {
        for (let j = 0; j < pharmacySalesData[i].length; j++) {
            Logger.log(pharmacySalesData[i][j]);
        }
    }

    Logger.log(bestSellers);
}

function loopOver2DArrayFiltered() {
    const pharmacySalesData = [
        ['Medicine', 'Quantity Sold', 'Revenue'],
        ['Aspirin', 100, 2000],
        ['Paracetamol', 150, 3000],
        ['Ibuprofen', 80, 1600],
    ];

    const bestSellers = [['Medicine', 'Quantity Sold']];

    for (let i = 1; i < pharmacySalesData.length; i++) {
        if (pharmacySalesData[i][1] >= 100) { 
            bestSellers.push([pharmacySalesData[i][0], pharmacySalesData[i][1]]);
        }
    }

    Logger.log(bestSellers);
}

function arrayModificationExample() {
    const inventory = [['Item', 'Quantity'], ['Screws', 100], ['Nails', 200]];
    inventory.push(['Bolts', 300]);
    inventory.unshift(['Item ID', '0001']);
    inventory.pop();
    inventory.shift();
    Logger.log(inventory);
}

function arrayAdvancedExample() {
    const inventory = [['Item', 'Quantity'], ['Screws', 100], ['Nails', 200]];
    const sliced = inventory.slice(1, 3);
    inventory.splice(1, 1, ['Bolts', 300]);
    delete inventory[2];
    Logger.log(sliced);
    Logger.log(inventory);
}

function arrayStringConversion() {
    const inventory = [['Item', 'Quantity'], ['Screws', 100], ['Nails', 200]];
    const stringified = JSON.stringify(inventory);
    const joined = inventory.join('; ');
    const parsed = JSON.parse(stringified);
    Logger.log(stringified);
    Logger.log(joined);
    Logger.log(parsed);
}

function forEachExample() {
    const sheetData = [['Product', 'Price'], ['Pen', 1.2], ['Notebook', 2.5]];

    function logEachRow(row, index) {
        if (index > 0) Logger.log(`Row ${index}: ${row[0]}, ${row[1]}`);
    }

    function iterateSheetData() {
        sheetData.forEach(logEachRow);
    }

    iterateSheetData();
}

function mapExample() {
    const sheetData = [['Product', 'Price'], ['Pen', 1.2], ['Notebook', 2.5]];

    function priceWithTax(row, index) {
        return index === 0 ? row : [row[0], row[1] * 1.1];
    }

    function applyTaxToPrices() {
        const updatedSheetData = sheetData.map(priceWithTax);
        Logger.log(updatedSheetData);
    }

    applyTaxToPrices();
}

function filterExample() {
    const sheetData = [['Product', 'Price'], ['Pen', 1.2], ['Notebook', 2.5]];

    function filterExpensiveItems(row) {
        return row[1] > 2;
    }

    function getExpensiveItems() {
        const expensiveItems = sheetData.filter(filterExpensiveItems);
        Logger.log(expensiveItems);
    }

    getExpensiveItems();
}

function reduceExample() {
    const sheetData = [['Product', 'Price'], ['Pen', 1.2], ['Notebook', 2.5]];

    function calculateTotalPrice(accumulator, row) {
        return typeof row[1] === 'number' ? accumulator + row[1] : accumulator;
    }

    function getTotalPrice() {
        const totalPrice = sheetData.reduce(calculateTotalPrice, 0);
        console.log(`Total Price: ${totalPrice}`);
    }

    getTotalPrice();
}

function highlightSpecificTasks() {
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    const ranges = ["A2:F2", "A5:F5", "A8:F8", "A11:F11"];

    const rangeList = sheet.getRangeList(ranges);
    rangeList.setBackground("yellow");
}

function updateBudgetSheet() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sheet = ss.getSheetByName("Budget");

  sheet.getRange("B2:B10").setValues(newExpenses);

  SpreadsheetApp.flush();

  const totalExpenses = calculateTotalExpenses();

  sheet.getRange("B11").setValue(totalExpenses);
}

const newExpenses = [
  [12.5],
  [9.99],
  [0],
  [30],
  [5],
  [14],
  [7],
  [3.50],
  [20]
];

function calculateTotalExpenses() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sheet = ss.getSheetByName("Budget");

  const values = sheet.getRange("B2:B10").getValues();
  return values.reduce((sum, row) => sum + (row[0] || 0), 0);
}

function createConditionalFormatExample() {
        const sheet = SpreadsheetApp.getActive().getActiveSheet();

        const range = sheet.getRange('A1:B3');

        const rule = SpreadsheetApp.newConditionalFormatRule()
        .whenNumberBetween(1, 10)
        .setBackground("#FF0000")
        .setRanges([range])
        .build();
        let rules = sheet.getConditionalFormatRules();

        rules.push(rule);

        sheet.setConditionalFormatRules(rules);
}
