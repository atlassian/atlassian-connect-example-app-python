/* globals $, AP */
const homePage = document.getElementById('homePage');
const configPage = document.getElementById('configPage');

if (homePage != null) {
    homePage.addEventListener('click', (event) => {
        event.preventDefault();
        AP.navigator.go('addonmodule', { moduleKey: 'acn-index' });
    });
}

if (configPage != null) {
    configPage.addEventListener('click', (event) => {
        event.preventDefault();
        AP.navigator.go('addonmodule', { moduleKey: 'acn-config' });
    });
}