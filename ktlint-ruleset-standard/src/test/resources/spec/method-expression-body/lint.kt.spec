class C0 {
    fun good(): Int = funcReturningInt()
    fun bad(): Int {
        return funcReturningInt()
    }
    fun bad2() {
        funcReturningNothing()
    }
}

fun goodFreeFunc() = funcReturningNothing()

fun badFreeFunc() {
    funcReturningNothing()
}

// expect
// 3:5:Single expression methods should use an expression body
// 6:5:Single expression methods should use an expression body
// 13:1:Single expression methods should use an expression body
