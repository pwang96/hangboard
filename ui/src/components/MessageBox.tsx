import { useState, useEffect } from "react";

import { MessageApi } from "../api/MessageApi";

function MessageBox() {
  const [message, setMessage] = useState("no message");
  useEffect(() => {
    MessageApi.getMessage().then((testResponse) => {
      setMessage(
        testResponse.message === undefined ? "" : testResponse.message,
      );
    });
  }, []);

  return (
    <div>
      <p>{message}</p>
    </div>
  );
}

export default MessageBox;
