from openai import OpenAI


class Assistant:
    def __init__(self, model: str = None, system: str = None):
        self.client = OpenAI()
        self.model = model or "gpt-3.5-turbo"
        self.system = system or "you are a source code generator"
        self.messages = [
            {"role": "system", "content": self.system},
        ]

    def chat(self, prompt: str, commit: bool = True) -> str:
        self.messages.append({"role": "user", "content": prompt})

        answer = (
            "Sure, here is an example Perl function that connects to AWS S3 using the `Paws` module:\n"
            + "\n"
            + "```perl\n"
            + "use Paws;\n"
            + "use Paws::Credential::ProviderChain;\n"
            + "\n"
            + "sub connect_to_s3 {\n"
            + "    my ($s3_bucket, $region) = @_;\n"
            + "\n"
            + "    my $s3 = Paws->new(\n"
            + "        config => {\n"
            + "            signature_version => 'V4',\n"
            + "            region => $region\n"
            + "        },\n"
            + "        credentials => Paws::Credential::ProviderChain->new(),\n"
            + "    );\n"
            + "\n"
            + "    my $result = $s3->ListObjects(Bucket => $s3_bucket);\n"
            + "\n"
            + "    if ($result) {\n"
            + '        print "Connected to S3 bucket $s3_bucket successfully\\n";\n'
            + "        return $s3;\n"
            + "    } else {\n"
            + '        die "Failed to connect to S3 bucket $s3_bucket\\n";\n'
            + "    }\n"
            + "}\n"
            + "\n"
            + "# Usage example:\n"
            + "my $s3 = connect_to_s3('your-bucket-name', 'us-east-1');\n"
            + "```\n"
            + "\n"
            + "Make sure to replace `'your-bucket-name'` and `'us-east-1'` with your actual S3 bucket name and the AWS "
            + "region where your bucket resides. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod "
            + "tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation "
            + "ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate "
            + "velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in "
            + "culpa qui officia deserunt mollit anim id est laborum."
        )

        if commit:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages,
            )
            answer = response.choices[0].message.content

        self.messages.append({"role": "assistant", "content": answer})

        return answer
