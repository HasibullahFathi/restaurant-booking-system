
/*!
* Start Bootstrap - Clean Blog v6.0.9 (https://startbootstrap.com/theme/clean-blog)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-clean-blog/blob/master/LICENSE)
*/
window.addEventListener('DOMContentLoaded', () => {
    let scrollPos = 0;
    const mainNav = document.getElementById('mainNav');
    const headerHeight = mainNav.clientHeight;
    window.addEventListener('scroll', function() {
        const currentTop = document.body.getBoundingClientRect().top * -1;
        if ( currentTop < scrollPos) {
            // Scrolling Up
            if (currentTop > 0 && mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-visible');
            } else {
                console.log(123);
                mainNav.classList.remove('is-visible', 'is-fixed');
            }
        } else {
            // Scrolling Down
            mainNav.classList.remove(['is-visible']);
            if (currentTop > headerHeight && !mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-fixed');
            }
        }
        scrollPos = currentTop;
    });

    const dateInput = document.getElementById('date');
    const shiftSelect = document.getElementById('shift');
    const tableSelect = document.getElementById('table');

    function updateAvailableTables() {
        const selectedShift = shiftSelect.value;
        const selectedDate = dateInput.value;

        if (selectedShift && selectedDate) {
            fetch(`/get_available_tables/?date=${selectedDate}&shift=${selectedShift}`)
                .then(response => response.json())
                .then(data => {
                    tableSelect.innerHTML = '<option value="">Select a table</option>';
                    data.tables.forEach(table => {
                        tableSelect.innerHTML += `<option value="${table.id}">${table.table_number}</option>`;
                    });
                })
                .catch(error => console.error('Error:', error));
        }
    }

    shiftSelect.addEventListener('change', updateAvailableTables);
    dateInput.addEventListener('change', updateAvailableTables);
})

