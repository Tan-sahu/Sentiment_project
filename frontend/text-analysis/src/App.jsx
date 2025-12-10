import { useState } from "react";
import { Container, Button, Card, Alert } from "react-bootstrap";

function App() {
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  const fetchData = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/api/data");
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      const data = await response.json();
      setMessage(JSON.stringify(data));
      setError("");
    } catch (err) {
      setError("Failed to connect to backend. Is it running?");
      console.error(err);
    }
  };

  return (
    <Container className="p-5">
      <h1 className="mb-4">React + FastAPI + Bootstrap</h1>

      <Card className="mb-3">
        <Card.Body>
          <Card.Title>Backend Connection Test</Card.Title>
          <Card.Text>
            Click the button below to fetch data from FastAPI.
          </Card.Text>
          <Button variant="primary" onClick={fetchData}>
            Fetch Data
          </Button>
        </Card.Body>
      </Card>

      {message && (
        <Alert variant="success">Response from Backend: {message}</Alert>
      )}

      {error && <Alert variant="danger">{error}</Alert>}
    </Container>
  );
}

export default App;
