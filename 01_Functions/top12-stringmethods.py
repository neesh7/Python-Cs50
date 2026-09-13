
"""
=====================================================
TOP 12 PYTHON STRING METHODS - Quick Reference + Demo
=====================================================
Strings are IMMUTABLE, so every method below RETURNS a new string.
The original is never changed unless you re-assign it:
    s.upper()        -> makes a new string, s is untouched
    s = s.upper()    -> s now points to the new string
"""

text = "  hello world from python  "
print("Original:", repr(text))  # repr shows the quotes + spaces clearly

# 1. strip() - remove whitespace (or given chars) from BOTH ends
# variants: lstrip() left only, rstrip() right only
print("1. strip()      ->", repr(text.strip()))
print("   rstrip()     ->", repr(text.rstrip()))
print("   strip('!')   ->", "wow!!!".strip("!"))  # strips the chars, not a word

s = text.strip()  # work with the cleaned version from here on

# 2. upper() / lower() - change case (useful for case-insensitive compares)
print("2. upper()      ->", s.upper())
print("   lower()      ->", "HeLLo".lower())

# 3. title() / capitalize() - capitalize each word / only the first letter
print("3. title()      ->", s.title())
print("   capitalize() ->", s.capitalize())

# 4. replace(old, new) - swap every occurrence; pass a count to limit it
print("4. replace()    ->", s.replace("world", "universe"))
print("   replace(n=1) ->", "a-b-c-d".replace("-", "+", 2))  # only first 2

# 5. split(sep) - string -> list. Default splits on any whitespace
print("5. split()      ->", s.split())          # ['hello','world','from','python']
print("   split(',')   ->", "a,b,c".split(","))  # ['a','b','c']

# 6. join(iterable) - list -> string. Called ON the separator
words = s.split()
print("6. join()       ->", "-".join(words))
print("   join spaces  ->", " ".join(["Python", "is", "fun"]))

# 7. find(sub) - index of first match, -1 if absent (index() raises an error)
print("7. find()       ->", s.find("world"))   # 6
print("   find missing ->", s.find("java"))    # -1  (safe, no crash)

# 8. count(sub) - how many non-overlapping times sub appears
print("8. count()      ->", s.count("o"))      # 4  -> hello, world, from, python
print("   count word   ->", "ha ha ha".count("ha"))

# 9. startswith() / endswith() - boolean checks, great in if-statements
print("9. startswith() ->", s.startswith("hello"))
print("   endswith()   ->", s.endswith(".py"))
print("   tuple check  ->", "notes.txt".endswith((".txt", ".md")))  # any of them

# 10. isdigit() / isalpha() / isalnum() - validate content before converting
print("10. isdigit()   ->", "12345".isdigit())   # True -> safe for int()
print("    isalpha()   ->", "Python".isalpha())  # True -> letters only
print("    isalnum()   ->", "abc123".isalnum())  # True -> letters + digits
print("    isspace()   ->", "   ".isspace())

# 11. zfill() / center() / ljust() / rjust() - padding & alignment
print("11. zfill(5)    ->", "42".zfill(5))            # 00042
print("    center(20)  ->", repr("menu".center(20, "*")))
print("    ljust(10)   ->", repr("name".ljust(10, ".")))

# 12. format() - placeholder substitution (the older cousin of f-strings)
print("12. format()    ->", "{} scored {} marks".format("Neesh", 95))
print("    by index    ->", "{0}-{1}-{0}".format("A", "B"))
print("    f-string    ->", f"{'Neesh'} scored {95} marks")  # preferred today


# --------- Chaining: methods return strings, so they can be linked ---------
messy = "   pRoGrAmMiNg In pYtHoN   "
print("Chained         ->", messy.strip().lower().title().replace(" In ", " with "))


# --------- Mini practical example: cleaning up user data ---------
raw_emails = ["  Neesh@Gmail.COM ", "ADMIN@site.org", " user@Mail.in  "]
clean = [e.strip().lower() for e in raw_emails]
print("Cleaned emails  ->", clean)

for email in clean:
    user, domain = email.split("@")          # split on the @ symbol
    print(f"  user={user.ljust(8)} domain={domain} valid={email.count('@') == 1}")
