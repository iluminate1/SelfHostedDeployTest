<script lang="ts">
    import { todosStore } from "../store/todos.svelte";
    import type { TodoCreate } from "@/types/todo";

    let content = $state("");
    let isAdding = $state(false);

    async function handleSubmit(event: Event) {
        event.preventDefault();
        if (content.trim() && !isAdding) {
            isAdding = true;
            const newTodo: TodoCreate = { content };
            await todosStore.addTodo(newTodo);
            content = "";
            isAdding = false;
        }
    }
</script>

<form onsubmit={handleSubmit} class="flex items-center">
    <input
        type="text"
        placeholder="What needs to be done?"
        bind:value={content}
        class="flex-1 bg-gray-50 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 text-gray-900 dark:text-white rounded-l-lg p-4 focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition-colors"
        disabled={isAdding}
    />
    <button
        type="submit"
        class="bg-blue-500 hover:bg-blue-600 dark:bg-blue-600 dark:hover:bg-blue-700 text-white font-medium rounded-r-lg px-5 py-4 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
        disabled={!content.trim() || isAdding}
    >
        {#if isAdding}
            <svg
                class="animate-spin -ml-1 mr-2 h-5 w-5 text-white inline"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
            >
                <circle
                    class="opacity-25"
                    cx="12"
                    cy="12"
                    r="10"
                    stroke="currentColor"
                    stroke-width="4"
                ></circle>
                <path
                    class="opacity-75"
                    fill="currentColor"
                    d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                ></path>
            </svg>
        {/if}
        Add
    </button>
</form>
