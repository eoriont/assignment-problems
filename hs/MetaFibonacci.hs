metaFibonacciSum :: (Integral a) => a -> a
metaFibonacciSum 0 = 0
metaFibonacciSum n = fib n + metaFibonacciSum (n -1)

fib :: (Integral a) => a -> a
fib 0 = 0
fib 1 = 1
fib n = fib (n -1) + fib (n -2)

main = print . metaFibonacciSum $ 6
