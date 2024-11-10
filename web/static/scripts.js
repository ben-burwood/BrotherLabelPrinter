document.getElementById('sizeInput').addEventListener('input', function () {
    const value = this.value;
    document.getElementById('sizeNumber').value = value;
});

document.getElementById('sizeNumber').addEventListener('input', function () {
    const value = this.value;
    document.getElementById('sizeInput').value = value;
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
