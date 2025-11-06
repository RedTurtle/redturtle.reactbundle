import React from 'react';
//import ReactDOM from 'react-dom';
import * as ReactDOM from 'react-dom/client';
import * as ReactDOMServer from 'react-dom/server.browser';
import * as ReactDOMLegacy from 'react-dom'; // <-- importa anche il modulo legacy

// --- React 19 createPortal shim ---
if (!ReactDOM.createPortal && ReactDOMLegacy.createPortal) {
  // aggiungiamo la vecchia API al namespace client
  ReactDOM.createPortal = ReactDOMLegacy.createPortal;
}
// --- end shim ---

window.React = React;
window.ReactDOM = ReactDOM;
window.ReactDOMServer = ReactDOMServer;
