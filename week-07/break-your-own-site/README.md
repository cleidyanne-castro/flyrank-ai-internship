# Break Your Own Site

I tested the live portfolio as if I had never opened it before.

## Test matrix

| Case | Expected result | Result |
| --- | --- | --- |
| English page | Page loads with a descriptive title | Passed |
| Portuguese page | Page loads without a broken navigation path | Passed |
| Empty form field | Browser blocks the submission | Passed by native validation |
| Invalid email | Browser blocks the submission | Passed by native validation |
| Project links | Each visible link opens a public destination | Passed |
| CV link | Public CV destination opens | Passed |
| Narrow viewport | Text and form remain usable without horizontal scrolling | Passed in browser viewport |
| Contact delivery | Message reaches the configured mailbox | Requires mailbox access |
| Custom domain | Domain resolves over HTTPS | Pending domain setup |

## Fixes

The site uses the current repository count, includes the Portuguese page, and points recruiter links to public destinations. The contact form now exposes its external data flow and reports the submission state.

## Limitations

The mailbox delivery check, physical phone check, and custom-domain check remain outside this repository evidence.
