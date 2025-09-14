import type { Todo, TodoCreate, TodoPatch, TodoCount } from "@/types/todo";

const API_URL = "/api";
const csrfTokenName: string = "x-csrftoken";
function getCSRFToken(): string {
  const metaTag = document.querySelector("meta[name=csrf-token]");
  const token = metaTag?.getAttribute("content") || "";
  return token;
}

export async function getTodos(): Promise<Todo[]> {
  const response = await fetch(`${API_URL}/todos`);
  return response.json();
}

export async function createTodo(todo: TodoCreate): Promise<Todo> {
  const response = await fetch(`${API_URL}/todos`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      [csrfTokenName]: getCSRFToken(),
    },
    body: JSON.stringify(todo),
  });
  return response.json();
}

export async function deleteTodo(todoId: number): Promise<void> {
  await fetch(`${API_URL}/todos/${todoId}`, {
    method: "DELETE",
    headers: {
      [csrfTokenName]: getCSRFToken(),
    },
  });
}

export async function updateTodo(
  todoId: number,
  updates: TodoPatch,
): Promise<Todo> {
  const response = await fetch(`${API_URL}/todos/${todoId}`, {
    method: "PATCH",
    headers: {
      "Content-Type": "application/json",
      [csrfTokenName]: getCSRFToken(),
    },
    body: JSON.stringify(updates),
  });
  return response.json();
}

export async function toggleTodoStatus(todoId: number): Promise<Todo> {
  const response = await fetch(`${API_URL}/todos/${todoId}/toggle`, {
    method: "PATCH",
    headers: {
      [csrfTokenName]: getCSRFToken(),
    },
  });
  return response.json();
}
