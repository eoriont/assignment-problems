fibonacciSum :: (Integral a) => a -> a
fibonacciSum n = sum [fib x | x <- [0 .. n]]

fib :: (Integral a) => a -> a
fib 0 = 0
fib 1 = 1
fib n = fib (n -1) + fib (n -2)

metaFibonacciSum :: (Integral a) => a -> a
metaFibonacciSum n = sum [fibonacciSum . fib $ x | x <- [0 .. n]]

main = print . metaFibonacciSum $ 6
