# Numeric-Processor
A Processor to calculate both computations from an api and a json file

Working in a scientific laboratory.

Your equipment performs measurements, and creates digital files containing data. You then need to run mathematical computations on this data, for the scientists to determine the results of the experiment. One of your computer systems produces the list of computations that need to be done. It creates a json file with contents like this:

```
{
    "computations":
    [
        {"operation": "add", "values": ["6.393504", "1.838937"]},
        {"operation": "multiply", "values": ["ANS", "4.659381"]},
        {"operation": "subtract", "values": ["ANS", "8.91116"]},
        {"operation": "display", "values": ["ANS"]}
        {"operation": "api-compute", "values": ["5*(4.847626-2.022232)"]}
        {"operation": "display", "values": ["ANS"]}
    ]
}
```

(The special string `ANS` means that you should use result of the previous computation that was done. The `api-compute` operation is a special operation that connects to an online server to do the computation - more on that later.)

```
{
    "computations":
    [
        {"operation": "add", "values": ["6.393504", "1.838937"]},
        {"operation": "multiply", "values": ["ANS", "4.659381"]},
        {"operation": "subtract", "values": ["ANS", "8.91116"]},
        {"operation": "display", "values": ["ANS"]}
    ]
}
```

If the program recieved the example above, it would do the following:

- Run `6.393504 + 1.838937` and store the result `8.232441`.
- Run `ANS * 4.659381`, which is `8.232441 * 4.659381`, and store the result `38.35808`.
- Run `ANS - 8.91141`, which is `38.35808 - 8.91116`, and store the result `29.446919`.
- Show the result `29.446919`.

### Using cloud computation

For processing large amounts of data, programmers will sometimes send the data over the internet so that it can be processed by servers in the cloud, for example sending the data to servers set up by Amazon Web Services.

These dedicated servers can be faster and more cost-effective for programmers, because it is expensive to set up and maintain your own group of servers.


<img src="cloud.png" width="10%" height="10%" style="border:none, border-width: 0, border: 0; box-shadow: 0px 0px;" />

Here is a sample input file:

```
{
    "computations": [
        {"operation": "api-compute", "values": ["5*(4.847626-2.022232)"]}
        {"operation": "display", "values": ["ANS"]}
    ]
}

```

If the program recieved the example above, it would do the following:

- Call the mathjs.org API and send the operation `"5*(4.847626-2.022232)"`
- Store the result `14.12697`.
- Show the result `14.12697`.

### Requirements

These are the types of processor operations that are supported, and what they should do.

```
"add"
    receives two numbers, add them

"multiply"
    receives two numbers, multiply them

"subtract"
    receives two numbers, subtract them

"divide"
    receives two numbers, divide them

"api-compute"
    receives a string, send it to the mathjs.org api and store the result

"display"
    receives one number, show it to the screen using print
```

After each operation, the result is stored, so that in the next line that comes up, `ANS` can be used to refer to the last result.