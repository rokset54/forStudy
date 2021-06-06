% rebase('layout.tpl', title=title, length=length, year=year)

<head>
	<link rel = "shortcut icon" href="https://atom.io/favicon.ico"/>
    <h2>{{ title }} </h2>
    <h3>{{ message }}</h3>
</head>
<style>

</style>
<body>

	<br>
	<br>
	<p style="font-size: 19px">
	Select the number of vertices in the graph</p>

	<form method="post">
	<table border="1">
	<input type="number" value="{{length}}" min="3" max="10" name="CHANGE" />
	<input class="btn btn-primary" type="submit" name="BTN" value="Enter" style="
    padding: 8px;
    color: red;
	background-color: white;
    border-radius: 15px;
	"/>



	</table>
	</form>


	<br>
	<br>
	

</body>

<address>
	<br>
	<br>
    <strong>Support:</strong>   <a href="mailto:sagas54@mail.ru">sagas54@mail.ru</a><br />
</address>
