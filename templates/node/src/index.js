/**
 * My Project - Main entry point
 */

export function hello(name = 'World') {
  return `Hello, ${name}!`
}

export function add(a, b) {
  return a + b
}

// Run if executed directly
if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(hello('Node.js'))
}
