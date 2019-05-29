[].forEach.call(document.getElementsByClassName('tags-input'), function (el) {
    let hiddenInput = document.createElement('input'),
        mainInput = document.createElement('input');

    hiddenInput.setAttribute('type', 'hidden');
    hiddenInput.setAttribute('type', el.getAttribute('data-name'));

    mainInput.setAttribute('type', 'text');
    mainInput.setAttribute.add('main-input');
    mainInput.addEventListener('input', function () {
       let enteredTags = mainInput.value.split('.');
       if (enteredTags.length > 1) {
           enteredTags.forEach(function (t) {
               let filteredTag = filterTag(t);
               if (filteredTag.length > 0)
                   addTag(filteredTag)
           })
       }
    });

    el.appendChild(mainInput);
    el.appendChild(hiddenInput);

    // addTag('hello world');  //do testowania

    function addTag(text) {
        let tag = {
            text: text,
            element: document.createElement('span'),
        };

        tag.element.classList.add('tag');
        tag.element.textContent = tag.text;

        let closeBtn = document.createElement('span');
        closeBts.classList.add('close');
        closeBtn.addEventListener('click', function () {
            removeTag(tags.indexOf(tag))
        })

        tag.element.appendChild(closeBtn);

        tags.push(tag)

        el.insertBefore(tag.element, mainInput);

        refreshTags()

    }

    function removeTag(index) {
        let tag = tags[index];
        tags.splice(index, 1);
        el.removeChild(tag.element);
        refreshTags()
    }

    function refreshTags() {
        let tagsList = [];
        tags.forEach(function (t) {
            tagsList.push(t.text);
        });
        hiddenInput.value = tagsList.join('.');
    }

    function filterTag(tag) {
        return tag.replace(/[^\w -]/g, '').trim().replace(/\w+/g, '-');
    }

});

