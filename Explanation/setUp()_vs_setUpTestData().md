# setUp() VS setUpTestData()
---

* setUpTestData() is called once at the beginning of the test run for class-level setup. You'd use this to create objects that aren't going to be modified or changed in any of the test methods.

* setUp() is called before every test function to set up any objects that may be modified by the test (every test function will get a "fresh" version of these objects).

__[Click Here To Learn More](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing#test_structure_overview)__