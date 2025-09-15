<script lang="ts">
    import { onMount } from "svelte";
    import { todosStore } from "../store/todos.svelte";
    import type { Todo } from "@/types/todo";

    let todos: Todo[] = $state([]);
    let isLoading = $state(true);
    let editingTodoId: number | null = $state(null);
    let editContent = $state("");
    let todosLength = $derived(todos.length);
    let completedTodosLength = $derived(
        todos.filter((item) => item.is_completed).length,
    );

    todosStore.subscribe(({ todos: value, isLoading: loading }) => {
        todos = value;
        isLoading = loading;
    });

    onMount(() => {
        todosStore.fetchTodos();
    });

    function handleDelete(todoId: number) {
        todosStore.removeTodo(todoId);
    }

    function handleToggle(todoId: number) {
        todosStore.toggleTodo(todoId);
    }

    function handleEdit(todoId: number) {
        const todo = todos.find((t) => t.id === todoId);
        if (todo) {
            editingTodoId = todoId;
            editContent = todo.content;
        }
    }

    async function handleSaveEdit() {
        if (editingTodoId !== null) {
            await todosStore.editTodo(editingTodoId, { content: editContent });
            editingTodoId = null;
            editContent = "";
        }
    }

    function handleCancelEdit() {
        editingTodoId = null;
        editContent = "";
    }
</script>

<div>
    <h1
        class="text-2xl font-bold text-gray-800 dark:text-white mb-6 flex items-center justify-center"
    >
        Your Todos
        {#if isLoading}
            <svg
                class="animate-spin ml-2 h-5 w-5 text-gray-500"
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
    </h1>

    {#if isLoading}
        <div class="space-y-3">
            {#each Array(3) as _}
                <div
                    class="h-14 bg-gray-200 dark:bg-gray-700 rounded-lg animate-pulse"
                ></div>
            {/each}
        </div>
    {:else if todos.length === 0}
        <div class="text-center py-10">
            <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-12 w-12 mx-auto text-gray-400 dark:text-gray-500 mb-3"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
            >
                <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width={2}
                    d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"
                />
            </svg>
            <p class="text-gray-500 dark:text-gray-400">
                No todos yet. Add one above to get started!
            </p>
        </div>
    {:else}
        <ul class="divide-y divide-gray-200 dark:divide-gray-700">
            {#each todos as todo (todo.id)}
                <li class="py-4 first:pt-0 last:pb-0 group">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center space-x-3 flex-1 min-w-0">
                            <button
                                onclick={() => handleToggle(todo.id)}
                                class={`flex-shrink-0 w-5 h-5 rounded-full border-2 flex items-center justify-center focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 dark:focus:ring-offset-gray-800 transition-colors
                                        ${
                                            todo.is_completed
                                                ? "bg-green-500 border-green-500 text-white"
                                                : "border-gray-300 dark:border-gray-600 hover:border-blue-500 dark:hover:border-blue-400"
                                        }`}
                                aria-label={todo.is_completed
                                    ? "Mark as incomplete"
                                    : "Mark as complete"}
                            >
                                {#if todo.is_completed}
                                    <svg
                                        xmlns="http://www.w3.org/2000/svg"
                                        class="h-3 w-3"
                                        viewBox="0 0 20 20"
                                        fill="currentColor"
                                    >
                                        <path
                                            fill-rule="evenodd"
                                            d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
                                            clip-rule="evenodd"
                                        />
                                    </svg>
                                {/if}
                            </button>
                            <button
                                type="button"
                                class={`text-gray-800 dark:text-gray-200 break-words min-w-0 cursor-pointer transition-colors ${todo.is_completed ? "line-through opacity-60" : ""}`}
                                onclick={() => handleToggle(todo.id)}
                                onkeydown={(e) =>
                                    e.key === "Enter" && handleToggle(todo.id)}
                                aria-label={todo.is_completed
                                    ? "Mark as incomplete"
                                    : "Mark as complete"}
                            >
                                {todo.content}
                            </button>
                        </div>
                        <div class="flex space-x-2">
                            <button
                                class="ml-4 text-gray-400 hover:text-blue-500 dark:text-gray-500 dark:hover:text-blue-400 p-1 rounded-full hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors opacity-0 group-hover:opacity-100 focus:opacity-100 focus:outline-none focus:ring-2 focus:ring-blue-500"
                                onclick={() => handleEdit(todo.id)}
                                aria-label="Edit todo"
                            >
                                <svg
                                    xmlns="http://www.w3.org/2000/svg"
                                    class="h-5 w-5"
                                    fill="none"
                                    viewBox="0 0 24 24"
                                    stroke="currentColor"
                                >
                                    <path
                                        stroke-linecap="round"
                                        stroke-linejoin="round"
                                        stroke-width={2}
                                        d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.536L16.732 3.732z"
                                    />
                                </svg>
                            </button>
                            <button
                                class="ml-4 text-gray-400 hover:text-red-500 dark:text-gray-500 dark:hover:text-red-400 p-1 rounded-full hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors opacity-0 group-hover:opacity-100 focus:opacity-100 focus:outline-none focus:ring-2 focus:ring-red-500"
                                onclick={() => handleDelete(todo.id)}
                                aria-label="Delete todo"
                            >
                                <svg
                                    xmlns="http://www.w3.org/2000/svg"
                                    class="h-5 w-5"
                                    fill="none"
                                    viewBox="0 0 24 24"
                                    stroke="currentColor"
                                >
                                    <path
                                        stroke-linecap="round"
                                        stroke-linejoin="round"
                                        stroke-width={2}
                                        d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"
                                    />
                                </svg>
                            </button>
                        </div>
                    </div>
                    {#if editingTodoId === todo.id}
                        <div class="mt-2 flex items-center space-x-2">
                            <input
                                type="text"
                                bind:value={editContent}
                                class="flex-1 bg-gray-50 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 text-gray-900 dark:text-white rounded-lg p-2 focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition-colors"
                            />
                            <button
                                class="bg-blue-500 hover:bg-blue-600 dark:bg-blue-600 dark:hover:bg-blue-700 text-white font-medium rounded-lg px-4 py-2 transition-colors"
                                onclick={handleSaveEdit}
                            >
                                Save
                            </button>
                            <button
                                class="bg-gray-500 hover:bg-gray-600 dark:bg-gray-700 dark:hover:bg-gray-600 text-white font-medium rounded-lg px-4 py-2 transition-colors"
                                onclick={handleCancelEdit}
                            >
                                Cancel
                            </button>
                        </div>
                    {/if}
                </li>
            {/each}
        </ul>

        <div
            class="mt-6 pt-4 border-t border-gray-200 dark:border-gray-700 flex justify-center text-sm text-gray-500 dark:text-gray-400"
        >
            <span>
                {completedTodosLength}
                of
                {todosLength}
                {todosLength === 1 ? "item" : "items"}
                completed
            </span>
        </div>
    {/if}
</div>
