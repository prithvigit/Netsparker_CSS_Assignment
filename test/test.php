<?php

 $dbhost = "localhost";
 $dbuser = "root";
 $dbpass = "";
 $db = "temp";
 $conn = new mysqli($dbhost, $dbuser, $dbpass,$db) or die("Connect failed: %s\n". $conn -> error);
 echo "The text recieved :";  
 echo $_POST["name"];
 $sql = "Select * from test where firstname = ".$_POST["name"];
 echo "<br> Executing query : ";
 echo $sql;
 if($result = mysqli_query($conn, $sql)){
    if(mysqli_num_rows($result) > 0){
        echo "<table>";
	while($row = mysqli_fetch_array($result)){
            echo "<tr>";
                echo "<td>" . $row['id'] . "</td>";
                echo "<td>" . $row['firstname'] . "</td>";
                echo "<td>" . $row['email'] . "</td>";
            echo "</tr>";
        }
        echo "</table>";
        // Free result set
        mysqli_free_result($result);
    } else{
        echo "No records matching your query were found.";
    }
} else{
    echo "ERROR: Could not able to execute $sql. " . mysqli_error($conn);
}
 function CloseCon($conn)
 {
 $conn -> close();
 }
   
?>