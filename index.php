<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Alexa Simulation</title>
</head>
<body>
    <h1>Alexa Simulation</h1>
    <form method="post" action="">
        <label for="command">Enter Command:</label>
        <input type="text" id="command" name="command" required>
        <button type="submit">Submit</button>
    </form>

    <?php
    if ($_SERVER['REQUEST_METHOD'] == 'POST') {
        $command = $_POST['command'];

        $url = 'http://127.0.0.1:5000/alexa';
        $data = array('command' => $command);

        // Use curl to send the command to the Python API
        $options = array(
            'http' => array(
                'header'  => "Content-Type: application/json\r\n",
                'method'  => 'POST',
                'content' => json_encode($data),
            ),
        );

        $context  = stream_context_create($options);
        $result = file_get_contents($url, false, $context);

        if ($result === FALSE) {
            echo '<p>Error occurred while processing the command.</p>';
        } else {
            $response = json_decode($result, true);
            echo '<p>Response: ' . htmlspecialchars($response['response']) . '</p>';
        }
    }
    ?>
</body>
</html>
