//
//  main.swift
//  comparison of exception handling speed
//
//  Created by Лю Пчела on 17.12.2021.
//
import CoreFoundation

class ParkBenchTimer {
    let startTime:CFAbsoluteTime
    var endTime:CFAbsoluteTime?

    init() {
        startTime = CFAbsoluteTimeGetCurrent()
    }

    func stop() -> CFAbsoluteTime {
        endTime = CFAbsoluteTimeGetCurrent()

        return duration!
    }

    var duration: CFAbsoluteTime? {
        if let endTime = endTime {
            return endTime - startTime
        } else {
            return nil
        }
    }
}

var i = 10_000_000
let timerWhileAndExceptionHandling = ParkBenchTimer()

while i > 0 {
    
    do {
        try 1
        
    } catch {
        1
    }
    
    i -= 1
}

let whileAndExceptionHandlingTime = timerWhileAndExceptionHandling.stop()
print("\(whileAndExceptionHandlingTime) seconds for while and exception handling.")


i = 10_000_000
let timerWhile = ParkBenchTimer()

while i > 0 {
    i -= 1
}

let whileTime = timerWhile.stop()
print("\(whileTime) seconds for while.")


let exceptionHandlingTime = whileAndExceptionHandlingTime - whileTime
print("\(exceptionHandlingTime) seconds for exception handling.")


// output:
// 0.8576210737228394 seconds for while and exception handling.
// 0.8481490612030029 seconds for while.
// 0.009472012519836426 seconds for exception handling.
// Program ended with exit code: 0

