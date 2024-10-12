# react-app-init

基于reskript构建的react前端项目初始化模板

## 安装

```shell
yarn
```

## 启动开发

```shell
yarn start
```

## 代码检查

```shell
yarn lint
```

设置有提交前的 Git Hook，会自动进行检查，如检查不通过无法提交代码。

## 构建

```shell
yarn build # 普通构建
yarn analyze # 构建后提供报告
```

## 配置

基于`reskript`的项目默认不会暴露 webpack 的配置文件，如需更改则可参考[reskript](https://reskript.dev/docs/getting-started) 的文档修改`reskript.config.js`