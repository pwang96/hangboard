import { useState, useEffect } from 'react';

import { Api } from '../gensrc/api/Api.ts';


const serviceBaseUrl = `${window.location.origin}`;
console.log(serviceBaseUrl);

const api = new Api( {
    baseUrl: "http://127.0.0.1:5000",
} );

function getMessage() {
    const hello = api.getHello().then(
        (value) => value,
        (error) => {console.log(error)}
    );
    console.log(hello);
    return hello;
}

function MessageBox(props) {
    const [message, setMessage] = useState("no message");
    useEffect(() => {
        setMessage(getMessage());
    }, []);


    return (
        <div>
            <p>{message}</p>
        </div>
    );
}

export default MessageBox;