<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1"> 

<title>Panel de control del auto</title>

  <!-- Bootstrap core CSS -->
  <link href="static/css/bootstrap.min.css" rel="stylesheet">

  <!-- Custom styles for this template -->
  <link href="static/css/jumbotron.css" rel="stylesheet">


<style media="screen" type="text/css">

.img-responsive {
    margin: 0 auto;
}
</style>


</head>


<body>
<div class="container">
<div class="jumbotron">
        <h1 align="center">Panel de control del auto</h1>
        <p class="lead" align="center">Control&aacute; el auto via WI-FI.</p>
        <p align="center"><a class="btn btn-lg btn-success" href="#" role="button">M&aacute;s informaci&oacute;n!</a></p>
</div>
</div>



<img src="static/images/robot.jpg" width="800" height="600" class="img-responsive" alt="Responsive image">


<h2 align="center">Controles del auto</h2>

<br>
<br>

<div class="container">
    <div class="row">
        <div class="col-sm-offset-6 col-sm-2">
		<button type="button" id="avanza" class="btn btn-default btn-lg" align="center">
		<span class="glyphicon glyphicon-menu-up" aria-hidden="true"></span></button>
	</div>
    </div>
    <div class="row">

        <div class="col-sm-offset-4 col-sm-2">
		<button type="button" id="izquierda" class="btn btn-default btn-lg">
		<span class="glyphicon glyphicon-menu-left" aria-hidden="true"></span></button>
	</div>


        <div class="col-sm-offset-0 col-sm-2"></div>


        <div class="col-sm-offset-0 col-sm-2">
		<button type="button" id="derecha" class="btn btn-default btn-lg">
		<span class="glyphicon glyphicon-menu-right" aria-hidden="true"></span></button>
	</div>



    </div>
    <div class="row">
        <div class="col-sm-offset-6 col-sm-2">
		<button type="button" id="reversa" class="btn btn-default btn-lg">
		<span class="glyphicon glyphicon-menu-down" aria-hidden="true"></span></button>
	</div>
    </div>
</div>

<br>

<div class="row">
<div class="col-md-offset-3 col-md-1">
		<button type="button" id="rotar_derecha" class="btn btn-default btn-lg">
		<span class="glyphicon glyphicon glyphicon-repeat" aria-hidden="true"></span> Rotar derecha</button>
</div>
<div class="col-md-offset-4 col-md-1">
		<button type="button" id="rotar_izq" class="btn btn-default btn-lg">
		<span class="glyphicon glyphicocon glyphicon-refresh " aria-hidden="true"></span> Rotar izquierda</button>
</div>
</div>


      <hr>

      <footer>
        <p align="center">&copy; 2017 Tuxedoar</p>
      </footer>


    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>

<script>
        $(document).ready(function() {
                $('#avanza').click(function() {
                        $.post('/avanza');
                });
                $('#reversa').click(function() {
                        $.post('/reversa');
                });

		 $('#derecha').click(function() {
                        $.post('/derecha');
                });
                $('#izquierda').click(function() {
                        $.post('/izquierda');
                });

                $('#rotar_derecha').click(function() {
                        $.post('/rotar_derecha');
                });

                $('#rotar_izq').click(function() {
                        $.post('/rotar_izq');
                });

        });

</script>


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <!-- <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script> -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>

</body>
</html>
