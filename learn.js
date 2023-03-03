/*
    1. Variable: var <variable_name>
    2. Comment: // or / * * /. Shortcut: Ctrl / or Alt Shift A or Enter /**
    3. Built-in function: console alert confirm prompt setTimeout setInterval
    4. Operator: 
        - Assignment Operators: =, +=, -=, *=, /=, %=, **=
        - Arithmetic Operators: +, -, *, /, %, ++, --, **
        - Comparison Operators: ==, !=, ===, !==, >, >=, <, <=
        - Logical Operators: &&, ||, !
        - String Operators: +, +=
        - Bitwise Operators: &, |, ^, ~, <<, >>, >>>
        - Other JavaScript Operators: typeof, ?: , in
    5. Boolean: Falsy: 0, false, '', "", undefined, NaN, null => false. Truthy: other
    6. Datatype:
        - Primitive data: number, string, boolean, undefined, null, symbol
        - Complex data: - Function
                        - Object: Object, Array
    7. Function: NOTE: arguments => all parameters of function
        - Declaration function - hoisted
        - Expression function
    8. String:
        - Method: length, indexOf, lastIndexOf, search, slice, replace, toUpperCase, toLowerCase, trim, split, charAt
        - template string `${<variable_name>}`
        - String includes
    9. Number:
        - type: IEEE-754, bigInt
        - Parse
        - e, toFixed
    10. Array:
        - length, []
    11. Object:
        - Object Constructor
        - Object prototype
        - Date, Math -> PI, round, abs, ceil, floor, random, min, max
    12. Conditional statements: 
        - if(){} else if(){} else{}
        - switch(){}
        - ternary operator: ?:
    13: Loop
        - For, For in (key), For of (value). Note: Object.keys(<object_name>), Object.value(<object_name>) -> array
        - While, Do While
        - Break, Continue, 
        - Nested Loop
        - Recursion (de quy): NOTE: Set
    14. Array methods: forEach, every, some, find, filter, map, reduce
        - Array includes
    15. Callback
    16. HTML DOM: (element, attribute, text)
        - Get Node:
            - Element: id, class, tagName, Css Selector, HTML Collection
            - Attribute:
                - setter: element.<valid_attr> = <value>
                - getter: element.<valid_attr>
                - element.getAttribute(<attr>)
                - element.setAttribute(<attr>, <value>)
            - Text:
                - get: element.innerText, element.textContent
                - set: element.innerText = <value>, element.textContent = <value>
                - Diff: innerText just text
        - InnerHTML, OuterHTML
        - Node Properties
        - DOM CSS
        - ClassList property
        - DOM events
            - Attributes events
            - Assign events using element nodes
            - NOTE: Event bubbling
            - Input, select, key up/down events
            - preventDefault, stopPropagation
            - Event listener
    17. JSON -> string
        - JSON.stringify, JSON.parse
    18. Promise (sync, async)
    - pain: Callback hell
    - new Promise
    - Promise methods
*/

var users = [{id: 1,name: 'John Doe',},{id: 2,name: 'Jackson',},{id: 3,name: 'Alice',}]

var comments = [{id: 1,text: 'This is a comment 1',user_id: 1,},{id: 2,text: 'This is a comment 2',user_id: 1,},{id: 3,text: 'This is a comment 3',user_id: 3,}]

var getComments = () => new Promise((resolve) => setTimeout(() => {resolve(comments)}, 3000))

var getUsersByIds = (userIds) => new Promise((resolve) => setTimeout(() => {
    resolve(users.filter((user) => userIds.includes(user.id)))
}, 5000))

getComments()
    .then(comments => {
        var userIds  = comments.map(comment => comment.user_id)
        return getUsersByIds(userIds)
            .then(users => ({users: users, comments: comments}))
    })
    .then(data => {
        var ul = document.querySelector('ul')
        data.comments.forEach(comment => {
            var user = data.users.find(user => user.id === comment.user_id)
            ul.innerHTML += `<li>${user.name}: ${comment.text}</li>`
        });
    })


