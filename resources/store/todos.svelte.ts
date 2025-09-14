import { writable } from "svelte/store";
import type { Todo, TodoCount, TodoCreate, TodoPatch } from "@/types/todo";
import {
  getTodos,
  createTodo,
  deleteTodo,
  updateTodo,
  toggleTodoStatus,
} from "../api";

const createTodosStore = () => {
  const { subscribe, set, update } = writable<Todo[]>([]);

  const fetchTodos = async () => {
    const todos = await getTodos();
    set(todos);
  };

  const addTodo = async (todo: TodoCreate) => {
    const newTodo = await createTodo(todo);
    update((todos) => [...todos, newTodo]);
  };

  const removeTodo = async (todoId: number) => {
    await deleteTodo(todoId);
    update((todos) => todos.filter((todo) => todo.id !== todoId));
  };

  const editTodo = async (todoId: number, updates: TodoPatch) => {
    const updatedTodo = await updateTodo(todoId, updates);
    update((todos) =>
      todos.map((todo) => (todo.id === todoId ? updatedTodo : todo)),
    );
  };

  const toggleTodo = async (todoId: number) => {
    const updatedTodo = await toggleTodoStatus(todoId);
    update((todos) =>
      todos.map((todo) => (todo.id === todoId ? updatedTodo : todo)),
    );
  };

  return {
    subscribe,
    fetchTodos,
    addTodo,
    removeTodo,
    editTodo,
    toggleTodo,
  };
};

export const todosStore = createTodosStore();
