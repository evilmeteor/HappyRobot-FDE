import { createSignal } from "solid-js";

import styles from "./App.module.css";

const App = () => {
  const [count, setCount] = createSignal(0);

  return (
    <main class={styles.container}>
      <header class={styles.hero}>
        <h1>HappyRobot Dashboard</h1>
        <p>Welcome! This SolidJS app will visualise data coming from the HappyRobot API.</p>
      </header>

      <section class={styles.card}>
        <p>
          This counter is just a placeholder component. Replace it with your first dashboard widget once the API is ready.
        </p>
        <button type="button" onClick={() => setCount(count() + 1)}>
          Count: {count()}
        </button>
      </section>
    </main>
  );
};

export default App;
