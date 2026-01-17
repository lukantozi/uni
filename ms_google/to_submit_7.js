function listFiles() {
    const files = DriveApp.getFiles();
    const fileNames = [];
    const MAX_FILES = 10;
    let fileCount = 0;
    while (files.hasNext() && fileCount < MAX_FILES) {
        fileNames.push(files.next().getName());
        fileCount++;
    }
    Logger.log(fileNames);
}

function listFiles() {
    const files = DriveApp.getFiles();
    const fileNamesTypes = [['File Name', 'Mime Type']];
    const MAX_FILES = 10;
    let fileCount = 0;
    while(files.hasNext() && fileCount < MAX_FILES) {
        const file = files.next();
        fileNamesTypes.push([file.getName(), file.getMimeType()]);
        fileCount++;
    }
    SpreadsheetApp
        .getActiveSheet()
        .getRange(1, 1, fileNamesTypes.length, fileNamesTypes[0].length)
        .setValues(fileNamesTypes)
}

function listFiles() {
    const ws = SpreadsheetApp.getActiveSheet();
    const mimeType = ws.getRange('D2').getValue();
    const files = !mimeType
        ? DriveApp.getFiles()
        : DriveApp.getFilesByType(mimeType)

    const fileNamesTypes = [['File Name', 'Mime Type']];
    const MAX_FILES = 10;
    let fileCount = 0;
    while (files.hasNext() && fileCount < MAX_FILES) {
        const file = files.next();
        fileNamesTypes.push([file.getName(), file.getMimeType()]);
        fileCount++;
    }

    ws.getRange(1, 1, fileNamesTypes.length, fileNamesTypes[0].length).setValues(
        fileNamesTypes
    );
}

function listContents() {
    const PARENT_FOLDER_ID = '2b67ae3da0a84cf38ff71dcbed29';
    const folder = DriveApp.getFolderById(PARENT_FOLDER_ID);
    const subfolders = iteratorToArray(folder.getFolders());
    const files = iteratorToArray(folder.getFiles());
    Logger.log(subfolders);
    Logger.log(files);
}

function iteratorToArray(iterator) {
    const array = [];
    while (iterator.hasNext()) {
        const item = iterator.next();
        const data = {
            id: item.getId(),
            name: item.getName(),
        };
        if (item.getMimeType) {
            data.mimeType = item.getMimeType();
        }
        array.push(data);
    }
    return array;
}

function run() {
    const PARENT_FOLDER_ID = '2b67ae3da0a84cf38ff71dcbed29';
    const fileTree = tree(PARENT_FOLDER_ID);
    Logger.log(JSON.stringify(fileTree, null, 2));
}

function tree(parentFolderId) {
    const recurse = ({ id, name }) => {
        const folder = DriveApp.getFolderById(id);
        const node = {
            id,
            name: name || folder.getName(),
            folders: iteratorToArray(folder.getFolders()),
            files: iteratorToArray(folder.getFiles()),
        };
        node.folders.forEach((folder, i) => {
            node.folders[i] = recurse(folder);
        });
        return node;
    };
    return recurse({ id: parentFolderId });
}

function drawTree(parentFolderId) {
    let str = '';
    const recurse = (node, depth = 0) => {
        str += `${' '.repeat(depth)}|— ${node.name}\n`;
        depth += 4;
        node.folders.forEach(folder => {
            recurse(folder, depth);
        });
        node.files.forEach(file => {
            str += `${' '.repeat(depth)}|— ${file.name}\n`;
        });
    };
    recurse(tree(parentFolderId));
    console.log(str);
}

function createFileInFolder() {
    const PARENT_FOLDER_ID = '2b67ae3da0a84cf38ff71dcbed29';
    const folder = DriveApp.getFolderById(PARENT_FOLDER_ID);
    folder.createFile('MyText.txt', 'Hello world!', MimeType.PLAIN_TEXT);
}

function createSpreadsheetInFolder() {
    const PARENT_FOLDER_ID = '2b67ae3da0a84cf38ff71dcbed29';
    const folder = DriveApp.getFolderById(PARENT_FOLDER_ID);
    const ss = SpreadsheetApp.create('My Spreadsheet');
    const file = DriveApp.getFileById(ss.getId());
    file.moveTo(folder);
}

function convertToPdf() {
    const fileId = '34302a7e83ff4f3fbaf0fedb39ec';
    const file = DriveApp.getFileById(fileId); 
    const blob = file.getAs('application/pdf');

    const folderId = '2b67ae3da0a84cf38ff71dcbed29'
    const folder = DriveApp.getFolderById(folderId);
    const newFile = folder.createFile(blob);

    Logger.log(newFile.getUrl());
    return newFile;
}

function createGmailDraftWithAttachment() {
    const fileId = '34302a7e83ff4f3fbaf0fedb39ec';
    const file = DriveApp.getFileById(fileId); 
    const blob = file.getAs('application/pdf');

    const draft = GmailApp.createDraft(
        'lmamrikishvili01@gmail.com',
        'An email with attachment',
        'Check the attachment',
        {
            attachments: [blob],
        }
    );
}
