var ale="";
function validate()
{
	var name=document.getElementById('name').value;
	if (!isNaN(name))
	{
		ale+="Please enter name";
	}


	if (ale!="")
	{
		alert(ale)
	}
	else
	{
		alert("Success")
	}
}
