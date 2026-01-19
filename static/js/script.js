// update the muscle group counter display
function updateMuscleCount() {
    const selectedBoxes = document.querySelectorAll('input[name="muscle_groups"]:checked');
    const totalCount = selectedBoxes.length;
    const counterElement = document.getElementById('muscleCount');
    // check if counter element exists
    if (counterElement) {
        let displayText = '';
        // check if singular or plural
        if (totalCount === 1) {
            displayText = totalCount + ' muscle group selected';
        } else {
            displayText = totalCount + ' muscle groups selected';
        }
        counterElement.textContent = displayText;
    }
}

// show or hide exercise details
function toggleExerciseDetails(muscle, exercise, event) {
    const checkbox = event.target;
    const divId = 'details_' + muscle + '_' + exercise;
    const detailsDiv = document.getElementById(divId);
    // show or hide based on checkbox
    if (checkbox.checked) {
        detailsDiv.style.display = 'flex';
    } else {
        detailsDiv.style.display = 'none';
    }
}

// toggle exercise section when muscle group is selected
function toggleExercises(muscle, event) {
    const checkbox = event.target;
    const sectionId = 'exercises_' + muscle;
    const exerciseSection = document.getElementById(sectionId);
    // show or hide the section
    if (checkbox.checked === true) {
        exerciseSection.style.display = 'block';
    } else {
        exerciseSection.style.display = 'none';
        // uncheck all exercise checkboxes in this section

        const allCheckboxes = exerciseSection.querySelectorAll('input[type="checkbox"]');
        for (let i = 0; i < allCheckboxes.length; i = i + 1) {
            allCheckboxes[i].checked = false;
        }

    }
    // call update function
    updateMuscleCount();
}

// get references to burger menu elements
const burgerMenu = document.getElementById('burgerMenu');
const mobileMenu = document.getElementById('mobileMenu');
// add click event to burger menu
burgerMenu.addEventListener('click', function () {
    mobileMenu.classList.toggle('active');
    burgerMenu.classList.toggle('active');
});
// get all navigation links
const navLinks = document.querySelectorAll('.mobile-menu a');
// add click event to each link
for (let i = 0; i < navLinks.length; i = i + 1) {
    navLinks[i].addEventListener('click', function () {
        // close the mobile menu
        mobileMenu.classList.remove('active');
        burgerMenu.classList.remove('active');
    });
}

