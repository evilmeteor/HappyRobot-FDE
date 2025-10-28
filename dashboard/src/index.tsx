import { render } from "solid-js/web";

import App from "./App";
import "./index.css";

const root = document.getElementById("root");

if (import.meta.env.DEV && !(root instanceof HTMLElement)) {
  throw new Error("Root element not found. Did you forget to add <div id=\"root\"></div> to index.html?");
}

render(() => <App />, root as HTMLElement);
