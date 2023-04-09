document.addEventListener("DOMContentLoaded", function() {
  const dropArea = document.querySelector(".drag-area");
  const dragFile = dropArea.querySelector(".drag-file");
  const input = dropArea.querySelector("[type='file']");
  let documentImages = document.querySelector("#document-images");

  let documentFileObj = {
    fileName: []
  };

  function nextButtonNavigation(sectionContainer) {
    sectionContainer.classList.add("hidden");
    sectionContainer.nextElementSibling.classList.add("block");
    sectionContainer.nextElementSibling.classList.remove("hidden");
  };

  function validationInputs (container, dataObject) {
    const errorMessage = container.querySelector("#input-empty-error");
    const emptyFields = [];

    for (const key in dataObject) {
      if (dataObject[key].length <= 0) {
        emptyFields.push(key.toUpperCase());
      }
    }
    
    errorMessage.textContent = 'Пожалуйста, выбрите минимум 1 файл';
    errorMessage.classList.remove("hidden");
    
    setTimeout(function () {
      errorMessage.classList.add("hidden");
    }, 2000);
  };

  input.addEventListener("change", function (e) {
    const target = e.target;

    setttingFileValue(target);
  });

  documentImages.addEventListener("click", function (e) {
    const target = e.target;
    const deleteFileButton = target.closest(".delete-document");
    const documentsWrapper = target.closest("#document-images");
    const documentToDelete = target.closest(".document-file");
    const documentName = documentToDelete.firstElementChild.children[1].innerText;

    if (deleteFileButton === null) return;

    const index = documentFileObj["fileName"].find((x) => x === documentName);

    documentFileObj["fileName"].splice(index, 1);
    documentsWrapper.removeChild(documentToDelete);
  });

  function fileTypeLogo(fileType) {
    if (fileType === "jpg" || fileType === "jpeg" || fileType === "png") return "text-violet-600 fa-image";

    return "text-red-600 fa-file-pdf";
  };

  dropArea.addEventListener("dragover", (event) => {
    event.preventDefault();
    dropArea.classList.add("active");
    dragFile.textContent = "Отпустите, чтобы загрузить файл";
  });

  dropArea.addEventListener("dragleave", function(){
    dropArea.classList.remove("active");
    dragFile.textContent = "Перетащите файл для загрузки";
  });

  dropArea.addEventListener("drop", (e) => {
    e.preventDefault();

    const target = e.dataTransfer;

    dropArea.classList.remove("active");
    dragFile.textContent = "Перетащите файл для загрузки";
    setttingFileValue(target);
  });

  document.querySelector("body").addEventListener("click", (e) => {
    const target = e.target;
    const nextButton = target.closest(".document-next-button");
    const sectionContainer = target.closest(".section-container");

    if (nextButton) {
      if (documentFileObj["fileName"].length !== 0) {
        nextButtonNavigation(sectionContainer);

        return;
      }

      validationInputs(sectionContainer, documentFileObj);
    }
  });

  function clear() {
    documentFileObj = {
      fileName: []
    };

    documentImages.textContent = '';
  }

  function setttingFileValue (target){
    const { files } = target;

    if (files.length === 0) return;

    clear();

    Array.from(files).forEach(file => {
      const fileName = file.name;
      const fileSize = file.size;
      const fileType = file.type.split("/").pop();

      let filetypeErrorMessage = document.getElementById("filetype-error");
      let sizeInMB = Number.parseFloat(fileSize / (1024 * 1024)).toFixed(2);

      const fileTypes = ["application/pdf","image/png","image/jpg","image/jpeg"]

      if (fileTypes.includes(file.type)) {
        filetypeErrorMessage.classList.add("hidden");

        let newDocument = document.createElement("li");

        newDocument.setAttribute(
          "class",
          "py-3 flex justify-between items-center md:items-end text-xs md:text-sm text-slate-700 border-b-2 border-slate-100 gap-1 document-file"
        );

        newDocument.innerHTML = `
              <p class="whitespace-nowrap overflow-hidden text-ellipsis w-40"><i class="fa-solid text-xl mr-5 ${fileTypeLogo(
                fileType
              )}"></i> 
                <span>${fileName}<span></p>
                <p>${fileType}</p>
                <p>${sizeInMB}mb</p>
                <p>Загружен</p>
                <button class="delete-document"><i class="fa-solid fa-trash"></i></button>
              `;

        documentImages.append(newDocument);
        documentFileObj["fileName"].push(fileName);

        return;
      }

      filetypeErrorMessage.classList.remove("hidden");
    });
  };
});