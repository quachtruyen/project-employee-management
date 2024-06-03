function handleBtnLogin() {
    console.log("click login")
    alert("1111");
    fetch(loginUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({ key: 'value' })
    })
    .then(response => response.text())
    .then(data => {
        console.log("departmnet")
        fetch(departmentUrl,{
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify({ key: 'value' })
        })
    });
}