## Interface

Charles 在线破解工具 https://www.zzzmode.com/mytools/charles/

接口自动化测试脚本
```text
测试过程：
    1.向测试数据库插入测试数据（一般使用测试数据库，不对真实数据库造成污染）;
    2.调用被测系统接口；
    3.接口对数据进行处理，并返回结果；
    4.通过python中的unittest单元测试框架断言接口返回的数据，并生成测试报告。
```

AppiumPython  客户端自动化测试

selleniumPython web自动化测试

### 以下是测试工具资料

1. UFT（别名：QuickTest Professional简称QTP）是一种自动化测试工具，以VBScirpt为内嵌语言
2. Robotium是基于instumentation 框架扩展的Android自动化测试库，主要针对Android平台的应用进行黑盒自动化测试，它提供了模拟各种手势操作（点击、长按、滑动等）、查找和断言机制的API，能够对各种控件进行操作。
3. TestNG是Java中的一个测试框架， 类似于JUnit 和NUnit, 功能都差不多， 只是功能更加强大，使用也更方便。

4. appium 是一个自动化测试开源工具，支持 iOS 平台和 Android 平台上的原生应用，web应用和混合应用

5. Selenium是一个用于Web应用程序测试的工具。Selenium测试直接运行在浏览器中，就像真正的用户在操作一样。

6. mitmproxy 就是用于 MITM 的 proxy，MITM 即中间人攻击（Man-in-the-middle attack）。用于中间人攻击的代理首先会向正常的代理一样转发请求，保障服务端与客户端的通信，其次，会适时的查、记录其截获的数据，或篡改数据，引发服务端或客户端特定的行为。

7. HTMLTestRunner 为unittest单元测试框架的扩展，利用它所提供的HTMLTestRunner()类来替换unittest单元测试框架的TextTestRunner()类，从而生成HTML格式的测试报告。
8. UIAutomator UI自动化测试，模拟操作，android4.1后推出。权限较低有些系统api不能调用。缺点：1. 测试脚本只能使用Java语言 2. 测试脚本要打包成jar或者apk包上传到设备上才能运行。
9. uiautomator2是一个可以使用Python对Android设备进行UI自动化的库。
10. instrumentation 主要是用于单元测试
11.Monkey是Android SDK提供的一个命令行工具，可以简单方便的发送伪随机的用户事件流，对Android APP做压力（稳定性）测试。主要是为了测试app是否存在无响应和崩溃的情况。

12. 质量保证：Process and Product Quality Assurance，即过程与产品质量保证。


12. monkeyrunner与Monkey:

- Monkey： android系统中自带的黑盒测试工具。一般通过随机触发界面事件，来确定应用是否会发生异常，多用于android应用的稳定性,压力测试。
- monkeyrunner：android SDK中自带的黑盒测试工具，在PC端通过android api 控制设备的运行，支持python脚本，可以实现monkey无法实现的逻辑功能
 
- Monkeyrunner缺点：
1、monkeyrunner本身存在bug，长时间跑，自身也会出现crash
2、monkeyrunner无论导入什么库，都是app层的，黑盒测试，相当于android ui layout上又架了一层，模拟点击操作




