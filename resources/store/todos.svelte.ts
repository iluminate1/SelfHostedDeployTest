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
  const { subscribe, set, update } = writable<{
    todos: Todo[];
    isLoading: boolean;
  }>({ todos: [], isLoading: true });

  const fetchTodos = async () => {
    update((state) => ({ ...state, isLoading: true }));
    const todos = await getTodos();
    set({ todos, isLoading: false });
  };

  const addTodo = async (todo: TodoCreate) => {
    const newTodo = await createTodo(todo);
    update((state) => ({ ...state, todos: [...state.todos, newTodo] }));
  };

  const removeTodo = async (todoId: number) => {
    await deleteTodo(todoId);
    update((state) => ({
      ...state,
      todos: state.todos.filter((todo) => todo.id !== todoId),
    }));
  };

  const editTodo = async (todoId: number, updates: TodoPatch) => {
    const updatedTodo = await updateTodo(todoId, updates);
    update((state) => ({
      ...state,
      todos: state.todos.map((todo) =>
        todo.id === todoId ? updatedTodo : todo,
      ),
    }));
  };

  const toggleTodo = async (todoId: number) => {
    const updatedTodo = await toggleTodoStatus(todoId);
    update((state) => ({
      ...state,
      todos: state.todos.map((todo) =>
        todo.id === todoId ? updatedTodo : todo,
      ),
    }));
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
