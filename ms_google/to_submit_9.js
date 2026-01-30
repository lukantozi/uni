function getPresentation() {
    const p1 = SlidesApp.getActivePresentation();
    const p2 = SlidesApp.openById('1bCYC6CknUqpt6RmeeYdKRgAjgdZzeS6iFMqSWm4rFK0');
    Logger.log(p1.getName());
    Logger.log(p2.getName());
}
function createPresentation() {
    const p = SlidesApp.create('Created with Apps Script');
    const url = p.getUrl();
    Logger.log(url);
}

function listSlides() {
    const p = SlidesApp.getActivePresentation();
    const slides = p.getSlides();
    const list = slides
        .reduce(
            (acc, slide, i) =>
            acc +
            `Index: ${i}, ID: ${slide.getObjectId()}, Page Type:
            ${slide.getPageType()}\n`,
            ""
        )
        .trim();
    Logger.log(list);
}
function duplicateSlideByIndex() {
    const p = SlidesApp.getActivePresentation();
    p.getSlides()[1].duplicate();
}

function duplicateSlideById() {
    const p = SlidesApp.getActivePresentation();
    p.getSlideById('g3932b5c48bb_0_0').duplicate();
}
function insertSlide() {
    const p = SlidesApp.getActivePresentation();
    p.insertSlide(1);
}
function insertSlide() {
    const p = SlidesApp.getActivePresentation();
    p.insertSlide (1, SlidesApp.PredefinedLayout.);
}
function insertSlide() {
    const p = SlidesApp.getActivePresentation();
    p.insertSlide (1, SlidesApp. PredefinedLayout.TITLE_AND_TWO_COLUMNS);
}

function insertSlideWithCustomLayout() {
    const p = SlidesApp.getActivePresentation();
    p.insertSlide (1, p.getLayouts()[12]);
}

function replaceText() {
    const p = SlidesApp.getActivePresentation();
    p.replaceAllText('Powerpoint', 'Google Slides');
}
SlidesApp.getActivePresentation().getMasters()[0].getLayouts();

function listLayouts() {
    const p = SlidesApp.getActivePresentation();
    const layouts = p.getLayouts();
    const list = layouts
        .reduce(
            (acc, layout, i) =>
            acc +
            `Index: ${i}, ID: ${layout.getObjectId()}, Page Type:
            ${layout.getPageType()}\n`,
        )
        .trim();
    Logger.log(list);
}
function importTheme() {
    const p = SlidesApp.getActivePresentation();
    const templateSlide = SlidesApp.openById(
        '14c2BHpAkJKI8PLtCg'
    ).getSlides()[0];
    const importedSlide = p.appendSlide (templateSlide);
    p.getMasters()[0].remove();
    importedSlide.remove();
}
