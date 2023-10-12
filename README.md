
---

# NLP Project 📖
**目的 (Purpose):**  
このリポジトリは、自然言語処理を取り扱うアプリケーションのソースコードを格納しています。  
This repository contains the source code for an application dealing with natural language processing.

---

## 🚀 環境構築 (Environment Setup)

このアプリケーションはDockerを利用しているため、簡単に環境を構築することができます。以下の手順をご参照ください。  
This application uses Docker, making it easy to set up the environment. Please follow the steps below.

### 1. 必要なライブラリのインストール (Installing Required Libraries):
- `requirements.txt` には、アプリケーションの実行に必要なライブラリがリストされています。  
The `requirements.txt` lists the libraries required to run the application.
  
- 開発用とデプロイ用にそれぞれ異なるライブラリをインストールする場合 (If installing different libraries for development and deployment):  
  - 開発用 (Development): `requirements.dev.txt`
  - デプロイ用 (Deployment): `requirements.prod.txt`

### 2. 環境変数の設定 (Setting up Environment Variables):
- 開発用 (Development): `.env.dev.sample` を参考にして `.env.dev` を作成。  
Use `.env.dev.sample` as a reference to create `.env.dev`.
  
- デプロイ用 (Deployment): `.env.prod.sample` を参考にして `.env.prod` を作成。  
Use `.env.prod.sample` as a reference to create `.env.prod`.

### 3. Dockerを利用した起動 (Starting with Docker):

#### 開発環境 (Development Environment):
```bash
docker-compose -f docker-compose.dev.yml build
docker-compose -f docker-compose.dev.yml up -d
```

#### デプロイ環境 (Deployment Environment):
```bash
docker-compose -f docker-compose.prod.yml build
docker-compose -f docker-compose.prod.yml up -d
```

---


