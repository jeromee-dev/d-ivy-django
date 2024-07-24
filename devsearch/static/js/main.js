// get search form and page links
const searchForm = document.getElementById('searchForm');
const pageLinks = document.getElementsByClassName('page-link');

// ensure that search form exists
if (searchForm) {
    for (const link of pageLinks) {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            // get the data attribute
            const page = this.dataset.page;
            console.log(`Current page: ${page}`);
            // add hidden search input to form
            searchForm.innerHTML += `<input value=${page} name="page" hidden>`
            // finally submit the form
            searchForm.submit();
        });
    }
}