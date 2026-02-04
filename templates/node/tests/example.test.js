import { describe, test, expect } from 'vitest'
import { hello, add } from '../src/index.js'

describe('hello', () => {
  test('greets with default name', () => {
    expect(hello()).toBe('Hello, World!')
  })

  test('greets with custom name', () => {
    expect(hello('Monty')).toBe('Hello, Monty!')
  })
})

describe('add', () => {
  test('adds two numbers', () => {
    expect(add(2, 3)).toBe(5)
  })

  test('handles negative numbers', () => {
    expect(add(-1, 1)).toBe(0)
  })
})
