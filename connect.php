<?php
// Database connection script
$host = "localhost";
$db = "users"; // Ensure this is your correct DB name
$user = "root";
$pass = ""; 

// Create connection
$conn = new mysqli($host, $user, $pass, $db);

// Check connection
if ($conn->connect_error) {
    if (isset($_SERVER['REQUEST_URI']) && strpos($_SERVER['REQUEST_URI'], 'api.php') !== false) {
        header("Content-Type: application/json");
        echo json_encode(["error" => true, "message" => "Database connection failed: " . $conn->connect_error, "db_connect_error_details" => $conn->connect_error]);
        exit;
    } else {
        die("Connection failed: " . $conn->connect_error);
    }
}

if (!$conn->set_charset("utf8")) {
    if (isset($_SERVER['REQUEST_URI']) && strpos($_SERVER['REQUEST_URI'], 'api.php') !== false) {
        header("Content-Type: application/json");
        echo json_encode(["error" => true, "message" => "Error loading character set utf8: " . $conn->error]);
        exit;
    } else {
    }
}
?>