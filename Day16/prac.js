function addData() {
    let empname = document.getElementById('empname').value;
    let empid = document.getElementById('empid').value;
    let empsalary = document.getElementById('empsalary').value;
    let empdept = document.getElementById('empdept').value;
    let tb = document.getElementById('empinfo')

    info = document.getElementById('empinfo');
    info.style.visibility = 'visible'

    tr = document.createElement('tr');
    aid = document.createAttribute('id');
    aid.value = `${empid}`
    tr.setAttributeNode(aid);
    // td = document.createElement('td');
    data = `<td>${empid}</td><td>${empname}</td><td>${empsalary}</td><td>${empdept}</td><td><button class="btn bg-danger btn-danger" onclick="deleteInfo(this)">X</button></td>`;
    tr.innerHTML = data;
    tb.appendChild(tr);
    document.getElementById('empname').value = ""
    document.getElementById('empid').value = ""
    document.getElementById('empsalary').value = ""
    document.getElementById('empdept').value = "Department"
}

function deleteInfo(button) {
    let row = button.parentElement.parentElement;
    row.remove();
}