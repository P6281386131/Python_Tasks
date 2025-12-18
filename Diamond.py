class A:
    def foo(self):
        return("foo() must be overridden")


class B(A):
    def foo(self):
        return "foo() from B"


class C(A):
    def foo(self):
        return "foo() from C"


class D(B, C):
    def foo(self):
        # Resolve ambiguity manually
        b_value = B.foo(self)
        c_value = C.foo(self)
        return f"D combines: {b_value} AND {c_value}"


# Runtime polymorphism
obj = D()
print(obj.foo())
