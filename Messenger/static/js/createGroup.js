const buttonCreate = document.getElementById("create")
const blurForm = document.getElementById("blurform")
const formCreateGroup = document.getElementById("createGroupForm")

const closePopup = document.getElementById("closepopup")

buttonCreate.addEventListener(
    "click",
    function(event) {
        blurForm.classList.remove("hideform")
        formCreateGroup.classList.remove("hideform")
    }
)

closePopup.addEventListener(
    "click",
    function() {
        blurForm.classList.add("hideform")
        formCreateGroup.classList.add("hideform")
        const contactsList = document.getElementById("contactsadd")
        contactsList.classList.remove("hideform")
        const selectedContacts = document.getElementById("selectedContacts")
        selectedContacts.classList.remove("hideform")
    }
)

let selecting = true

const buttonCreateSubmit = document.getElementsByClassName("next")[0]

buttonCreateSubmit.addEventListener(
    "click",
    function() {
        if (buttonCreateSubmit.type == "button") {
            const contactsList = document.getElementById("contactsadd")
            contactsList.classList.add("hideform")
            const selectedContacts = document.getElementById("selectedContacts")
            selectedContacts.innerText = "Учасники"
            
            const hiddenInput = document.getElementById("selected_ids");
            hiddenInput.value = selectedContactsArray.join(",");
            let contacts = []
            const contactsListDiv = document.getElementById("contactsSelectedd")
            selectedContactsArray.forEach((id) => {
                const checkbox = document.querySelector(`input[name='contactsAdded'][value='${id}']`);
                if (checkbox) {
                    const label = checkbox.closest("label.contact");
                    if (label) {
                        label.style.display = "flex";
                        contacts.push(label)
                        console.log(contacts)
                        contactsListDiv.insertAdjacentElement('beforeend',label)
                    }
                }
            });
            contactsListDiv.classList.add("contactsadd")
            contactsListDiv.classList.remove("hideform")
            const imgSearch = document.getElementById("searchImg")
            const nameGroup = document.getElementById("nameGroup")
            nameGroup.placeholder = "Назва групи"
            imgSearch.remove()  
            const avatarGroup = document.getElementById("avatar-group")
            avatarGroup.classList.add("avatar-group")
            selecting = false
            buttonCreateSubmit.remove()
            document.getElementById("submit").classList.remove("hideform")
            document.getElementById("submit").classList.add("next")
        }

    }
)
let selectedContactsArray = [];

const updateSelectedCount = () => {
    const selectedCountElement = document.getElementById("selectedContacts");
    console.log(selectedContactsArray)
    selectedCountElement.innerText = `Вибрано: ${selectedContactsArray.length}`;
};

document.querySelectorAll("input[name='contactsAdded']").forEach((checkbox) => {
    checkbox.addEventListener("change", function () {
        const contactId = this.value;

        if (this.checked) {
            if (!selectedContactsArray.includes(contactId)) {
                selectedContactsArray.push(contactId);
            }
        } else {
            selectedContactsArray = selectedContactsArray.filter(id => id !== contactId);
        }

        updateSelectedCount();
    });
});