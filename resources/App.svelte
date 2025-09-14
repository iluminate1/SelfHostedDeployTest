<script lang="ts">
    import TodoList from "./lib/TodoList.svelte";
    import TodoForm from "./lib/TodoForm.svelte";
    import { onMount } from "svelte";

    let darkMode = false;

    onMount(() => {
        const saved = localStorage.getItem("darkMode");
        const systemPrefersDark = window.matchMedia(
            "(prefers-color-scheme: dark)",
        ).matches;

        if (saved !== null) {
            darkMode = saved === "true";
        } else {
            darkMode = systemPrefersDark;
        }

        updateTheme();
    });

    function toggleDarkMode() {
        darkMode = !darkMode;
        localStorage.setItem("darkMode", darkMode.toString());
        updateTheme();
    }

    function updateTheme() {
        if (darkMode) {
            document.documentElement.classList.add("dark");
        } else {
            document.documentElement.classList.remove("dark");
        }
    }
</script>

<svelte:head>
    <script>
        if (
            localStorage.getItem("darkMode") === "true" ||
            (!localStorage.getItem("darkMode") &&
                window.matchMedia("(prefers-color-scheme: dark)").matches)
        ) {
            document.documentElement.classList.add("dark");
        } else {
            document.documentElement.classList.remove("dark");
        }
    </script>
</svelte:head>

<main class="min-h-screen bg-gray-50 dark:bg-gray-900 transition-colors duration-300 flex items-center justify-center">
    <div class="container mx-auto px-4 py-8 max-w-2xl">
        <div class="flex justify-between items-center mb-8">
            <h1 class="text-3xl font-bold text-gray-800 dark:text-white">
                Todos List
            </h1>
            <button
                onclick={toggleDarkMode}
                class="p-2 rounded-full bg-gray-200 dark:bg-gray-700 text-gray-700 dark:text-gray-200 hover:bg-gray-300 dark:hover:bg-gray-600 transition-colors"
                aria-label="Toggle dark mode"
            >
                {#if darkMode}
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        class="h-6 w-6"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                    >
                        <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            stroke-width={2}
                            d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"
                        />
                    </svg>
                {:else}
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        class="h-6 w-6"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                    >
                        <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            stroke-width={2}
                            d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"
                        />
                    </svg>
                {/if}
            </button>
        </div>
        <div class="bg-white dark:bg-gray-800 rounded-xl shadow-lg p-6 mb-6 transition-colors duration-300">
            <TodoForm />
        </div>
        <div class="bg-white dark:bg-gray-800 rounded-xl shadow-lg p-6 transition-colors duration-300">
            <TodoList />
        </div>
    </div>
</main>