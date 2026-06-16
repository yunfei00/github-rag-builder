---
source: dify
owner: langgenius
repo: dify
path: docs/de-DE/CONTRIBUTING.md
url: https://github.com/langgenius/dify/blob/main/docs/de-DE/CONTRIBUTING.md
---
# MITWIRKEN

Sie möchten also zu Dify beitragen - das ist großartig, wir können es kaum erwarten zu sehen, was Sie entwickeln. Als Startup mit begrenztem Personal und Finanzierung haben wir große Ambitionen, den intuitivsten Workflow für die Entwicklung und Verwaltung von LLM-Anwendungen zu gestalten. Jede Hilfe aus der Community zählt wirklich.

Wir müssen wendig sein und schnell liefern, aber wir möchten auch sicherstellen, dass Mitwirkende wie Sie eine möglichst reibungslose Erfahrung beim Beitragen haben. Wir haben diesen Leitfaden zusammengestellt, damit Sie sich schnell mit der Codebasis und unserer Arbeitsweise mit Mitwirkenden vertraut machen können.

Dieser Leitfaden ist, wie Dify selbst, in ständiger Entwicklung. Wir sind dankbar für Ihr Verständnis, falls er manchmal hinter dem eigentlichen Projekt zurückbleibt, und begrüßen jedes Feedback zur Verbesserung.

Bitte nehmen Sie sich einen Moment Zeit, um unsere Lizenz- und Mitwirkungsvereinbarung zu lesen. Die Community hält sich außerdem an den Verhaltenskodex.

## Bevor Sie loslegen

Suchen Sie nach einer Aufgabe? Durchstöbern Sie unsere Einsteiger-Issues und wählen Sie eines zum Einstieg!

Haben Sie eine neue Modell-Runtime oder ein Tool hinzuzufügen? Öffnen Sie einen PR in unserem Plugin-Repository.

Möchten Sie eine bestehende Modell-Runtime oder ein Tool aktualisieren oder Bugs beheben? Besuchen Sie unser offizielles Plugin-Repository!

Vergessen Sie nicht, in der PR-Beschreibung ein bestehendes Issue zu verlinken oder ein neues zu erstellen.

### Fehlermeldungen

> [!WICHTIG]
> Bitte stellen Sie sicher, dass Sie folgende Informationen bei der Einreichung eines Fehlerberichts angeben:

- Ein klarer und beschreibender Titel
- Eine detaillierte Beschreibung des Fehlers, einschließlich Fehlermeldungen
- Schritte zur Reproduktion des Fehlers
- Erwartetes Verhalten
- **Logs** bei Backend-Problemen (sehr wichtig, zu finden in docker-compose logs)
- Screenshots oder Videos, falls zutreffend

Unsere Priorisierung:

| Fehlertyp | Priorität |
| ------------------------------------------------------------ | --------------- |
| Fehler in Kernfunktionen (Cloud-Service, Login nicht möglich, Anwendungen funktionieren nicht, Sicherheitslücken) | Kritisch |
| Nicht-kritische Fehler, Leistungsverbesserungen | Mittlere Priorität |
| Kleinere Korrekturen (Tippfehler, verwirrende aber funktionierende UI) | Niedrige Priorität |

### Feature-Anfragen

> [!HINWEIS]
> Bitte stellen Sie sicher, dass Sie folgende Informationen bei der Einreichung einer Feature-Anfrage angeben:

- Ein klarer und beschreibender Titel
- Eine detaillierte Beschreibung des Features
- Ein Anwendungsfall für das Feature
- Zusätzlicher Kontext oder Screenshots zur Feature-Anfrage

Unsere Priorisierung:

| Feature-Typ | Priorität |
| ------------------------------------------------------------ | --------------- |
| Hochprioritäre Features (durch Teammitglied gekennzeichnet) | Hohe Priorität |
| Beliebte Feature-Anfragen aus unserem Community-Feedback-Board | Mittlere Priorität |
| Nicht-Kernfunktionen und kleinere Verbesserungen | Niedrige Priorität |
| Wertvoll, aber nicht dringend | Zukunfts-Feature |

## Einreichen Ihres PRs

### Pull-Request-Prozess

1. Repository forken
1. Vor dem Erstellen eines PRs bitte ein Issue zur Diskussion der Änderungen erstellen
1. Einen neuen Branch für Ihre Änderungen erstellen
1. Tests für Ihre Änderungen hinzufügen
1. Sicherstellen, dass Ihr Code die bestehenden Tests besteht
1. Issue in der PR-Beschreibung verlinken (`fixes #`)
1. Auf den Merge warten!

### Projekt einrichten

#### Frontend

Für die Einrichtung des Frontend-Service folgen Sie bitte unserer ausführlichen Anleitung in der Datei `web/README.md`.

#### Backend

Für die Einrichtung des Backend-Service folgen Sie bitte unseren detaillierten Anweisungen in der Datei `api/README.md`.

#### Weitere Hinweise

Wir empfehlen, dieses Dokument sorgfältig zu lesen, da es wichtige Informationen enthält über:

- Voraussetzungen und Abhängigkeiten
- Installationsschritte
- Konfigurationsdetails
- Häufige Problemlösungen

Bei Problemen während der Einrichtung können Sie sich gerne an uns wenden.

## Hilfe bekommen

Wenn Sie beim Mitwirken Fragen haben oder nicht weiterkommen, stellen Sie Ihre Fragen einfach im entsprechenden GitHub Issue oder besuchen Sie unseren Discord für einen schnellen Austausch.
