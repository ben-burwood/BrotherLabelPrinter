document.getElementById('sizeInput').addEventListener('input', function () {
    const value = this.value;
    document.getElementById('sizeNumber').value = value;
});

document.getElementById('sizeNumber').addEventListener('input', function () {
    const value = this.value;
    document.getElementById('sizeInput').value = value;
});

document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("collapsePaddingBtn").addEventListener("click", function () {
        document.getElementById("paddingGrp").classList.toggle("active");
    });
});

function clearText() {
    document.getElementById('textInput').value = '';
}

function printViaApi() {
    const printButton = document.getElementById('printButton');
    printButton.disabled = true;

    const form = document.getElementById('printForm');
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    data.padding = {
        left: parseInt(data.padding_left),
        top: parseInt(data.padding_top),
        right: parseInt(data.padding_right),
        bottom: parseInt(data.padding_bottom)
    };
    delete data.padding_left;
    delete data.padding_top;
    delete data.padding_right;
    delete data.padding_bottom;

    fetch('/print', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
        .then(response => response.json())
        .then(result => {
            console.log('Success:', result);
        })
        .catch(error => {
            console.error('Error:', error);
        })
        .finally(() => {
            printButton.disabled = false;
        });
}
