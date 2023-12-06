import React, { useState } from 'react';
import { TextField } from '@mui/material'
import './App.css';
import axios from 'axios';

function App() {
  const [content, setContent] = useState("");
  const [question, setQuestion] = useState("");
  return (
    <div className="App">
      <div className="App-content">
        {content}
      </div>
      <TextField
        placeholder="You message here..."
        variant="standard"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        onKeyDown={(ev) => {
          if (ev.key === 'Enter') {
            setContent(content + `You: ${question}\n`);
            ev.preventDefault();
            axios.post("http://localhost:8000/ask", {question})
            .then((res) => {
              setContent(content + `You: ${question}\n` + `Bot: ${res.data}\n`);
              setQuestion("");
            })
            .catch((e) => {
              console.log(e);
            })
          }
        }}
      />
    </div>
  );
}

export default App;
